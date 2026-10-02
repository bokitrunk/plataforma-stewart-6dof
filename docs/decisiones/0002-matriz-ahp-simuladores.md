# ADR 0002: Matriz de Decisión AHP para Selección de Simulador de Vuelo RPA

* **Fecha:** 2026-09-30
* **Estado:** Propuesto / En Evaluación
* **Autores:** Benjamín, Javier Aguayo

---

## Contexto
Para el desarrollo del banco de pruebas Hardware-in-the-Loop (HITL), se requería evaluar y seleccionar la plataforma de software que ofreciera el mejor balance entre fidelidad aerodinámica, latencia de transmisión de telemetría e integración con el autopiloto Pixhawk.

Siguiendo la recomendación del profesor Alejandro López, se aplicaron criterios cualitativos y cuantitativos inspirados en la metodología AHP (Analytic Hierarchy Process) para comparar las siguientes alternativas: 

---

## Alternativas a evaluar
* **X-Plane:** Simulador actual basado en Blade Element Theory.
* **FlightGear:** Simulador de código abierto.
* **SimNet Aero:** Software dedicado a la simulación de RPAs ([SimNet Aero](https://www.simnet.aero)).
* **Matlab / Simulink:** Entorno de desarrollo de modelos dinámicos ([Aerospace Blockset](https://la.mathworks.com/products/aerospace-blockset.html) y [UAV Toolbox](https://la.mathworks.com/products/uav.html)).

---

## Criterios de Evaluación y Ponderación

1. **Latencia y frecuencia de transmisión (milisegundos):** Velocidad para enviar datos de actitud hacia la plataforma.
2. **Capacidad de intervención y código abierto:** Permite modificar o extender la física de vuelo e interfaces.
3. **Motor gráfico:** Capacidad de inspeccionar de forma visual e intuitiva la aeronave simulada.
4. **Fidelidad y adaptabilidad para RPAs:** Representatividad de modelos dinámicos para aeronaves pequeñas.

---

## Decisión
Se decide adoptar MATLAB / Simulink como la plataforma principal de cálculo, modelado de dinámica de vuelo y simulación de sensores IMU del proyecto, utilizando FlightGear como motor gráfico de animación en bucle secundario.

---

## Justificación técnica
1. **Unificación en una sola plataforma:** MATLAB permite ejecutar la dinámica de vuelo, el modelado de ruido/bias de sensores IMU, el filtro washout y la cinemática inversa de la plataforma Stewart dentro del mismo entorno.
2. **Tiempo real integrado:** Uso de Simulink Desktop Real-Time para garantizar tasas de refresco constantes y transmisiones UDP en milisegundos hacia el microcontrolador.
3. **Bloques nativos para FlightGear:** La Aerospace Blockset incluye bloques de comunicación listos para enviar datos de actitud a FlightGear sin necesidad de middleware de terceros.
4. **Licencia institucional:** Disponibilidad completa de las toolboxes especializadas gracias al convenio de la universidad.

---

## Consecuencias
**Positivas:** Reducción drástica del error por jitter en el envío de datos, modelado realista de ruido de sensores sin código manual adicional y compatibilidad directa con C/C++ auto-generado para el controlador (ESP32).

**A considerar:** Los archivos fuente principales en src/ pasarán de scripts en Python a modelos de Simulink (.slx) y scripts de apoyo en MATLAB (.m).