# ADR 0001: Implementación de Filtro Washout para el eje Yaw

* **Fecha:** 2026-09-30
* **Estado:** Aceptado

## Contexto
La plataforma Stewart de 6 GDL posee un espacio de trabajo físicamente limitado por la carrera de los 6 actuadores lineales. Al simular maniobras sostenidas de una aeronave (como giros continuos o aceleraciones prolongadas), los actuadores alcanzarían sus límites mecánicos rápidamente.

Para resolver esto, se requiere un algoritmo de Motion Cueing (Filtro Washout) que transmita las sensaciones inerciales de alta frecuencia al autopiloto y luego "lave" (retorne) suavemente la plataforma a su posición neutral por debajo del umbral de percepción humana.

## Decisión
Se decide implementar el Filtro Washout Clásico dentro del entorno MATLAB/Simulink, aplicando filtros pasa-altos (high-pass) para las aceleraciones/velocidades angulares y pasa-bajos (low-pass) para la inclinación por gravedad (tilt coordination).

## Consecuencias
- **Positivas:** Permite sintonizar las frecuencias de corte ($f_c$) y amortiguamiento directamente en el dominio de Laplace ($s$) en Simulink, facilitando la simulación continua sin saturar los actuadores..
- **A considerar:** Los parámetros del filtro se definirán como variables globales en un script de inicialización .m en src/matlab/ antes de ejecutar el modelo de Simulink.