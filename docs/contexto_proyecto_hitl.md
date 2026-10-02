# 📄 Contexto del Proyecto: Banco de Pruebas HITL con Plataforma Stewart 6-DOF

---

## 1. Declaración del Problema & Brecha de Realismo

### Definición del Problema
Evaluar algoritmos de control para vehículos aéreos pilotados remotamente (RPAs) mediante pruebas de vuelo reales es extremadamente **costoso, complejo e inseguro**, con un alto riesgo de pérdida de material.

### La "Brecha de Realismo" (SITL vs. HITL)
Las simulaciones puramente digitales conocidas como **Software-in-the-Loop (SITL)** inyectan señales sintéticas e ideales directamente al microcontrolador a través de software. Este enfoque omite por completo la respuesta física real de los sensores inerciales (IMUs) ante el movimiento, ocultando fenómenos físicos críticos como:
- Ruido mecánico de alta frecuencia generado por la estructura y motores.
- Vibraciones del sistema de propulsión.
- Histéresis mecánica y latencia real de muestreo de las IMUs.
- Acumulación de deriva (*drift*) en giroscopios y comportamiento no ideal de acelerómetros.

---

## 2. Definición Formal de Objetivos

### Objetivo General
Diseñar e implementar un banco de pruebas **Hardware-in-the-Loop (HITL)** compuesto por una plataforma Stewart a escala (6 GDL), integrando un simulador de dinámica de vuelo en **Matlab/Simulink (Aerospace/UAV Toolbox)** representativo para RPAs. La plataforma debe ser capaz de estimular físicamente los sensores (IMUs) de un autopiloto **Pixhawk con ArduPilot**.

### Objetivos Específicos
1. **Diseño mecatrónico:** Diseñar la estructura mecánica, selección de actuadores, electrónica de control y modelo de cinemática inversa, según la caracterización de la envolvente dinámica del RPA.
2. **Integración middleware y control:** Integrar la estructura física, electrónica de control y código, garantizando la conversión y transmisión de consignas de posición desde el simulador de vuelo a la plataforma en el orden de milisegundos (ms).
3. **Simulación especializada de RPA:** Implementar y parametrizar los modelos de dinámica y caracterización de sensores (IMU) usando MATLAB Aerospace Toolbox y FlightGear como motor gráfico.
4. **Evaluación de Sensores:** Evaluar la respuesta del autopiloto Pixhawk (ArduPilot) en lazo cerrado ante perturbaciones inerciales reales, comparando la estimación de actitud física frente a un entorno puramente simulado (SITL).

---

## 3. Arquitectura del Sistema e Integración

### Clarificación de Montaje Físico
> **Nota de Arquitectura:** El elemento montado sobre la plataforma móvil Stewart de 6-DOF es el **autopiloto (Pixhawk)** con sus sensores inerciales integrados, **NO la estructura física del RPA completa**. La plataforma actúa como un estimulador inercial físico para la suite sensorial del autopiloto.

### Lazo de Flujo de Datos (Lazo Cerrado)
```text
┌──────────────────────────────────────────────────────────┐
│              MATLAB / Simulink Environment               │
│  [Modelo Dinámico RPA (Aerospace / UAV Toolbox)]         │
│  [Modelo de Sensores IMU (Ruido, Drift, Bias)]           │
└──────────────┬────────────────────────────┬──────────────┘
               │ UDP Animation              │ Consignas l1..l6 (UDP)
               ▼                            ▼
   [ FlightGear Render 3D ]       [ Controlador ESP32 ]
                                            │ PWM / Actuadores
                                            ▼
                               [ Plataforma Stewart 6-DOF ]
                                            │ Movimiento Físico
                                            ▼
                               [ Autopiloto Pixhawk / ArduPilot ] 
```

### 4. Alcance y prioridades del semestre
**Fase actual:** Construcción y validación del modelo de cinemática inversa y filtro washout en MATLAB/Simulink, asegurando la transmisión UDP estable hacia el controlador físico.

**Fase futura:** Integración y validación completa del lazo HITL en el Laboratorio de Técnicas Aeroespaciales (LTA).