# ADR 0002: Matriz de Decisión AHP para Selección de Simulador de Vuelo RPA

* **Fecha:** 2026-09-30
* **Estado:** Propuesto / En Evaluación
* **Autores:** Benjamín, Javier Aguayo

---

## Contexto
Para el desarrollo del banco de pruebas HITL, se requiere evaluar alternativas de simuladores de vuelo dedicados o adaptables a aeronaves de pequeña escala (RPAs)[cite: 3]. Se busca seleccionar la plataforma de software que ofrezca el mejor balance entre fidelidad aerodinámica, latencia de transmisión de telemetría e integración con el autopiloto Pixhawk[cite: 3].

Siguiendo la recomendación del profesor Alejandro López, se aplicará la metodología **AHP (Analytic Hierarchy Process)** para estructurar la matriz de decisión[cite: 3].

---

## Criterios de Evaluación y Ponderación

1. **Latencia y Frecuencia de Transmisión (Milisegundos):** Velocidad para enviar datos de actitud hacia la plataforma[cite: 3].
2. **Capacidad de Intervención y Código Abierto:** Permite modificar o extender la física de vuelo e interfaces[cite: 3].
3. **Motor Gráfico:** Capacidad de inspeccionar de forma visual e intuitiva la aeronave simulada[cite: 3].
4. **Fidelidad y Adaptabilidad para RPAs:** Representatividad de modelos dinámicos para aeronaves pequeñas[cite: 3].

---

## Alternativas Evaluadas
* **X-Plane:** Simulador actual basado en Blade Element Theory[cite: 3].
* **FlightGear:** Simulador de código abierto[cite: 3].
* **SimNet Aero:** Software dedicado a simulación de RPAs (https://www.simnet.aero)[cite: 3].
* **Matlab / Simulink (Aerospace Blockset & UAV Toolbox):** Entorno de desarrollo de modelos dinámicos (https://la.mathworks.com/products/aerospace-blockset.html)[cite: 3].

---

## Decisiones Pendientes y Siguientes Pasos
- [ ] Ejecutar las comparaciones pareadas de Saaty para los criterios definidos[cite: 3].
- [ ] Validar la matriz resultante con los profesores patrocinantes (Bernardo, Cornejo)[cite: 3].