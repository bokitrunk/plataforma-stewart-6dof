# 🚁 Plataforma Gough-Stewart 6-DOF (Gemelo Digital & Simulación)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Estado-En_Desarrollo-orange.svg)]()
[![License](https://img.shields.io/badge/Licencia-MIT-green.svg)]()

Bienvenido al repositorio central del proyecto **Diseño e implementación de una plataforma Stewart para simulaciones de vuelo  de aeronaves no tripuladas​**. Este proyecto semestral abarca el diseño, la simulación matemática en tiempo real (*Gemelo Digital*) y el control físico de una plataforma de movimiento articulada por 6 actuadores independientes, alimentada por datos de telemetría de vuelo en tiempo real desde **X-Plane** vía comunicación UDP.

---

## 📌 Características Principales

* **Simulación Cinemática Inversa:** Cálculo en tiempo real de la longitud necesaria de cada uno de los 6 actuadores ($l_1 \dots l_6$) en base a posiciones $(X, Y, Z)$ y rotaciones ($\text{pitch}, \text{roll}, \text{yaw}$).
* **Filtro Washout Dinámico (Pasa-Altos):** Implementación de decaimiento dinámico (`ALPHA_WASHOUT = 0.92`) para simular sensaciones de aceleración angular en el eje Yaw sin saturar los límites mecánicos.
* **Integración con X-Plane:** Recepción de paquetes de telemetría vía red (UDP) con detección de arranque sin saltos bruscos (`raw_yaw_prev = None`).
* **Visualización 3D:** Renderizado vectorial en 3D del chasis base y la plataforma superior articulada.

---

## 📁 Estructura del Repositorio

```text
plataforma-stewart-6dof/
├── docs/                       # Documentación técnica y memoria del proyecto
│   ├── bibliografia/           # Papers, data-sheets y manuales técnicos (PDFs)
│   ├── decisiones/             # Registros de Decisiones de Arquitectura (ADRs)
│   └── matematica_geometria.md # Apuntes sobre matrices y cinemática
├── src/                        # Código fuente principal
│   └── modelo.py               # Script de simulación y renderizado 3D
├── tests/                      # Pruebas unitarias de las funciones matemáticas
├── .gitignore                  # Archivos ignorados por Git
└── README.md                   # Documentación principal del proyecto