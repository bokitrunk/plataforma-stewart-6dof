# ADR 0002: Matriz de Decisión AHP para Selección de Simulador de Vuelo RPA

* **Fecha:** 2026-09-30
* **Estado:** Propuesto / En Evaluación
* **Autores:** Benjamín, Javier Aguayo

---

## Contexto
Para el desarrollo del banco de pruebas HITL, se requiere evaluar alternativas de simuladores de vuelo dedicados o adaptables a aeronaves de pequeña escala (RPAs). Se busca seleccionar la plataforma de software que ofrezca el mejor balance entre fidelidad aerodinámica, latencia de transmisión de telemetría e integración con el autopiloto Pixhawk.

Siguiendo la recomendación del profesor Alejandro López, se aplicará la metodología **AHP (Analytic Hierarchy Process)** para estructurar la matriz de decisión.

---

## Criterios de Evaluación y Ponderación

1. **Latencia y Frecuencia de Transmisión (Milisegundos):** Velocidad para enviar datos de actitud hacia la plataforma.
2. **Capacidad de Intervención y Código Abierto:** Permite modificar o extender la física de vuelo e interfaces.
3. **Motor Gráfico:** Capacidad de inspeccionar de forma visual e intuitiva la aeronave simulada.
4. **Fidelidad y Adaptabilidad para RPAs:** Representatividad de modelos dinámicos para aeronaves pequeñas.

---

## Alternativas a evaluadar
* **X-Plane:** Simulador actual basado en Blade Element Theory.
* **FlightGear:** Simulador de código abierto.
* **SimNet Aero:** Software dedicado a la simulación de RPAs ([SimNet Aero](https://www.simnet.aero)).
* **Matlab / Simulink:** Entorno de desarrollo de modelos dinámicos ([Aerospace Blockset](https://la.mathworks.com/products/aerospace-blockset.html) y [UAV Toolbox](https://la.mathworks.com/products/uav.html)).

---

## Decisiones Pendientes y Siguientes Pasos
- [ ] Ejecutar las comparaciones pareadas de Saaty para los criterios definidos.
- [ ] Validar la matriz resultante con los profesores patrocinantes (Bernardo, Cornejo).