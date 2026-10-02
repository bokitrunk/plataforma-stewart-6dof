# 📋 Guía operativa: Bitácora de Reuniones y Sincronización con Planner

Esta guía establece el protocolo para registrar las inquietudes, avances y acuerdos del equipo durante las reuniones con los profesores patrocinantes y el trabajo presencial en el LTA.

---

## Protocolo de registro de bitácora

### 1. Actas de reunión con profesores
Después de cada reunión con Bernardo, Tinapp o docentes de la asignatura, se debe anotar:
* **Acuerdos y correcciones:** Ajustes a los problemas planteados o alcance.
* **Lista de conceptos clave:** Términos o dudas para discutir en la siguiente sesión.
* **Tareas inmediatas:** Acciones asignadas a los integrantes del equipo.

### 2. Trabajo presencial en el LTA
* Asistir periódicamente al **Laboratorio de Técnicas Aeroespaciales (LTA)** para trabajar en equipo, probar componentes y familiarizarse con la infraestructura.

---

## Sincronización con Planner y Carta Gantt
1. **Paso de tareas a Planner:** Toda tarea aprobada o definida en las reuniones debe transferirse inmediatamente desde la Carta Gantt hacia la herramienta **Microsoft Planner** del equipo.
2. **Asignación por habilidades:** Distribuir las actividades semanales según las fortalezas individuales de los integrantes del equipo.
3. **Puntos de control:** Revisar el cumplimiento de tareas previo a cada presentación oficial de avance.

### Estado de avance y seguimiento de tareas
- **Fase:** Modelado matemático y configuración de entorno SITL.
- **Plataforma:** Gough-Stewart de 6 grados de libertad (6-DOF).
- **Entorno:** Matlab/Simulink + FlighGear.

## Seguimiento de tareas
**Sprint 1:** Setup, repositorio y arquitectura base (completado)
- [x] Migración de arquitectura a Matlab/Simulink (ADR 0002).
- [x] Restructuración del repositorio (src/matlab/, src/simulink/, docs/decisiones/).
- [x] Actualización de contexto HITL, ADR 0001 y README.md.

**Sprint 2:** Parametrización geométrico-mecánica e Inversa (.m) (en curso).
- [ ] Definición del script de geometría de la plataforma Stewart (src/matlab/parametros_plataforma.m).
- [ ] Implementación de la función de cinemática inversa $l_1 \dots l_6$.
- [ ] Validación numérica de límites de carrera y espacio de trabajo (workspace).

**Sprint 3:** Modelo dinámico y filtro washout en Simulink 
- [ ] Modelo integrando actitud (roll, pitch, yaw).
- [ ] Sintonización del Filtro Washout en Simulink (ADR 0001).
- [ ] Bloques de comunicación UDP (FlightGear y ESP32).
