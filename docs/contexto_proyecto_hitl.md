# 📄 Contexto del Proyecto: Banco de Pruebas HITL con Plataforma Stewart 6-DOF

---

## 1. Declaración del Problema & Brecha de Realismo

### Definición del Problema
Evaluar algoritmos de control para Vehículos Aéreos Pilotados Remotamente (RPAs) mediante pruebas de vuelo reales es extremadamente **costoso, complejo e inseguro**, con un alto riesgo de pérdida de material.

### La "Brecha de Realismo" (SITL vs. HITL)
Las simulaciones puramente digitales conocidas como **Software-in-the-Loop (SITL)** inyectan señales sintéticas e ideales directamente al microcontrolador a través de software. Este enfoque omite por completo la respuesta física real de los sensores inerciales (IMUs) ante el movimiento, ocultando fenómenos físicos críticos como:
- Ruido mecánico de alta frecuencia generado por la estructura y motores[cite: 3].
- Vibraciones del sistema de propulsión[cite: 3].
- Histéresis mecánica y latencia real de muestreo de las IMUs[cite: 3].
- Acumulación de deriva (*drift*) en giroscopios y comportamiento no ideal de acelerómetros[cite: 3].

---

## 2. Definición Formal de Objetivos

### Objetivo General
Diseñar e implementar un banco de pruebas **Hardware-in-the-Loop (HITL)** compuesto por una plataforma Stewart a escala (6 GDL), integrando un simulador de dinámica de vuelo representativo para RPAs[cite: 3]. La plataforma debe ser capaz de estimular físicamente los sensores (IMUs) de un autopiloto **Pixhawk con ArduPilot**[cite: 3].

### Objetivos Específicos
1. **Diseño Mecatrónico:** Diseñar la estructura mecánica, selección de actuadores, electrónica de control y modelo de cinemática inversa, según la caracterización de la envolvente dinámica del RPA[cite: 3].
2. **Integración Middleware y Control:** Integrar la estructura física, electrónica de control y código, garantizando la conversión y transmisión de consignas de posición desde el simulador de vuelo a la plataforma en el orden de milisegundos (ms)[cite: 3].
3. **Selección de Simulador Especializado:** Evaluar y seleccionar un simulador de dinámica de vuelo alternativo (o dedicado) adaptado a las características aerodinámicas de aeronaves pequeñas tipo RPA[cite: 3].
4. **Evaluación de Sensores:** Evaluar la respuesta del autopiloto Pixhawk (ArduPilot) en lazo cerrado ante perturbaciones inerciales reales, comparando la estimación de actitud física frente a un entorno puramente simulado (SITL)[cite: 3].

---

## 3. Arquitectura del Sistema e Integración

### Clarificación de Montaje Físico
> **Nota de Arquitectura:** El elemento montado sobre la plataforma móvil Stewart de 6-DOF es el **autopiloto (Pixhawk)** con sus sensores inerciales integrados, **NO la estructura física del RPA completa**[cite: 3]. La plataforma actúa como un estimulador inercial físico para la suite sensorial del autopiloto[cite: 3].

### Lazo de Flujo de Datos (Lazo Cerrado)
```text
[ Simulador de Vuelo RPA ]
           │ Telemetría (milisegundos)
           ▼
[ Middleware / Filtro Washout ]
           │ Consignas Cinemática Inversa (l1..l6)
           ▼
[ Controlador / ESP32 ]
           │ Señales PWM / Control de Actuadores
           ▼
[ Plataforma Stewart 6-DOF ] (Movimiento Físico)
           │ Estimulación Inercial
           ▼
[ Autopiloto Pixhawk / ArduPilot ] (Fusión de Sensores - Filtro de Kalman)