# ADR 0001: Implementación de Filtro Washout para el eje Yaw

* **Fecha:** 2026-09-30
* **Estado:** Aceptado

## Contexto
El eje Yaw en X-Plane es continuo (0° a 360°). La plataforma física 6-DOF no puede rotar indefinidamente debido a las restricciones mecánicas de los actuadores.

## Decisión
Implementar un filtro pasa-altos dinámico con `ALPHA_WASHOUT = 0.92` y detección del primer fotograma con `raw_yaw_prev = None`.

## Justificación
- `raw_yaw_prev = None` evita saltos bruscos al arrancar la simulación cuando aún no hay lecturas previas.
- `ALPHA_WASHOUT = 0.92` conserva el 92% del impulso angular instantáneo y drena el 8% restante en cada paso de tiempo, devolviendo la plataforma al centro de forma suave e imperceptible.