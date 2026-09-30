---
name: seleccion-tecnologica
description: Proceso estructurado para la evaluación y selección de tecnologías, hardware, controladores y simuladores mediante el método AHP (Analytic Hierarchy Process). Usar al tomar decisiones de arquitectura o herramientas para proyectos mecatrónicos y de simulación.
---

# 🎯 Selección Tecnológica y Análisis de Decisiones (AHP)

Esta skill define el procedimiento para evaluar y seleccionar componentes tecnológicos, software o hardware en proyectos mecatrónicos mediante matrices de decisión AHP.

---

## 🛠️ Cuándo Usar Esta Skill
* Selección de simuladores de dinámica de vuelo (p. ej., JSBSim, X-Plane, FlightGear, AirSim).
* Selección de microcontroladores y placas de desarrollo (p. ej., ESP32, STM32, Arduino, Raspberry Pi).
* Selección de sensores inerciales o autopilotos (p. ej., Pixhawk, CubeOrange, Navio2).
* Documentación de decisiones arquitectónicas clave en el repositorio (`docs/decisiones/`).

---

## 📋 Pasos del Procedimiento

### 1. Definición de Criterios y Alternativas
* Establecer de 3 a 5 criterios de evaluación clave (ej. Precisión/Fidelidad, Facilidad de Integración, Latencia/Rendimiento, Licencia/Costo, Soporte de la Comunidad).
* Listar las alternativas tecnológicas candidatas.

### 2. Construcción de la Matriz AHP (Ponderación)
* Realizar la comparación pareada entre criterios usando la escala de Saaty (1 a 9).
* Calcular los pesos relativos ($w_i$) de cada criterio garantizando un Índice de Consistencia ($CI < 0.1$).

### 3. Evaluación de Alternativas
* Calificar cada alternativa frente a cada criterio.
* Calcular el puntaje ponderado total para cada candidato.

### 4. Documentación
* Generar el documento markdown correspondiente dentro del directorio `docs/decisiones/` (ejemplo: `docs/decisiones/01_seleccion_simulador.md`).
* Incluir la justificación cualitativa y la matriz cuantitativa resultante.