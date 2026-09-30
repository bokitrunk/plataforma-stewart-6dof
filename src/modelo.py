import socket
import struct
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# --- CONFIGURACIÓN UDP X-PLANE ---
UDP_IP = "127.0.0.1"
UDP_PORT = 49005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False)

# --- GEOMETRÍA DE LA PLATAFORMA STEWART ---
r_B = 0.20  # Radio de la base [m]
r_P = 0.12  # Radio de la plataforma móvil [m]
h0  = 0.25  # Altura inicial [m]

# Posición de los puntos de anclaje de la base y la plataforma en coordenadas polares o radianes
gamma_B = np.array([40, 140, 160, 260, 280, 20]) * np.pi / 180 # Posiciones angulares de los puntos de anclaje de la base (en radianes)
gamma_P = np.array([80, 100, 200, 220, 320, 340]) * np.pi / 180 # Posiciones angulares de los puntos de anclaje de la plataforma (en radianes)

# Posiciones en [metros] de los puntos de anclaje de la base y la plataforma en coordenadas cartesianas (X, Y, Z)
B = np.array([[r_B * np.cos(a), r_B * np.sin(a), 0] for a in gamma_B])
P_local = np.array([[r_P * np.cos(a), r_P * np.sin(a), 0] for a in gamma_P])

# Creación de 3 líneas vacías para guardar los ángulos de pitch, roll y yaw recibidos desde X-Plane
pitch, roll, yaw = 0.0, 0.0, 0.0

# --- VARIABLES DEL FILTRO WASHOUT DINÁMICO ---
raw_yaw_prev = None # en "None" es una carpeta vacía (ausencia de medida) y va así porque en 0.0° indica se dirige en rumbo 0° (avión con dirección y sentido hacia el norte)
yaw_filtrado = 0.0 # Aquí se almacena el ángulo de yaw filtrado por el filtro Washout
ALPHA_WASHOUT = 0.92  # factor de decaimiento del filtro Washout (0 < ALPHA_WASHOUT < 1)

def get_rotation_matrix(pitch_deg, roll_deg, yaw_deg):
    p_rad, r_rad, y_rad = np.radians([pitch_deg, roll_deg, yaw_deg])
    
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(p_rad), -np.sin(p_rad)],
                   [0, np.sin(p_rad), np.cos(p_rad)]])
    
    Ry = np.array([[np.cos(r_rad), 0, np.sin(r_rad)],
                   [0, 1, 0],
                   [-np.sin(r_rad), 0, np.cos(r_rad)]])
    
    Rz = np.array([[np.cos(y_rad), -np.sin(y_rad), 0],
                   [np.sin(y_rad), np.cos(y_rad), 0],
                   [0, 0, 1]])
    
    return Rz @ Ry @ Rx

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
fig.canvas.manager.set_window_title('Gemelo Digital - Plataforma Stewart 6-DOF')

def leer_udp():
    global pitch, roll, yaw, raw_yaw_prev, yaw_filtrado
    try:
        while True:
            data, _ = sock.recvfrom(1024)
            if data.startswith(b'DATA'):
                for i in range(5, len(data), 36):
                    chunk = data[i:i+36]
                    if len(chunk) == 36:
                        idx = struct.unpack('<I', chunk[:4])[0]
                        vals = struct.unpack('<8f', chunk[4:])
                        if idx == 17:
                            pitch = vals[0]
                            roll = vals[1]
                            raw_yaw = vals[2]

                            if raw_yaw_prev is None:
                                raw_yaw_prev = raw_yaw

                            # 1. Velocidad / Variación instantánea de rumbo (Delta)
                            delta_yaw = (raw_yaw - raw_yaw_prev + 180) % 360 - 180
                            raw_yaw_prev = raw_yaw

                            # 2. Filtro Washout (Pasa-Altos): Reacciona al cambio rápido y decae a cero poco a poco
                            yaw_filtrado = (yaw_filtrado + delta_yaw) * ALPHA_WASHOUT

                            # 3. Saturación física de seguridad
                            yaw = np.clip(yaw_filtrado, -12.0, 12.0)
    except Exception:
        pass

def update(frame):
    leer_udp()

    R = get_rotation_matrix(pitch, roll, yaw)
    T = np.array([0, 0, h0])
    P_global = np.array([T + R @ p for p in P_local])
    
    ax.cla()
    ax.set_xlim([-0.3, 0.3])
    ax.set_ylim([-0.3, 0.3])
    ax.set_zlim([0, 0.4])
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y - Frente (m)')
    ax.set_zlabel('Z (m)')
    
    titulo = f"Gemelo Digital | Pitch: {pitch:5.1f}° | Roll: {roll:5.1f}° | Yaw (Washout): {yaw:5.1f}°"
    ax.set_title(titulo)

    # Base (Verde)
    poly_base = Poly3DCollection([B], facecolors='forestgreen', alpha=0.35, edgecolors='darkgreen', linewidths=2)
    ax.add_collection3d(poly_base)

    # Plataforma (Azul)
    poly_plat = Poly3DCollection([P_global], facecolors='dodgerblue', alpha=0.6, edgecolors='navy', linewidths=2)
    ax.add_collection3d(poly_plat)

    # 6 Actuadores (Rojo)
    for i in range(6):
        ax.plot([B[i, 0], P_global[i, 0]],
                [B[i, 1], P_global[i, 1]],
                [B[i, 2], P_global[i, 2]], 'r-', linewidth=2.5)

ani = FuncAnimation(fig, update, interval=30, cache_frame_data=False)

plt.show()