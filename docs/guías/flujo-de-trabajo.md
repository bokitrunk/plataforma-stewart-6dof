---
name: flujo-de-trabajo
description: Guía de flujo de trabajo Git y estándares de documentación para proyectos mecatrónicos y de ingeniería. Usar al crear nuevas funcionalidades, commits, Pull Requests o gestionar documentación técnica.
---

# 🔄 Flujo de Trabajo Git y Gestión de Repositorio

Esta skill establece las pautas de control de versiones, nomenclatura de ramas y estándares de commits para mantener la trazabilidad y calidad del código y la documentación del proyecto.

---

## 🛠️ Cuándo Usar Esta Skill
* Creación y gestión de ramas de trabajo (`feature/`, `docs/`, `fix/`).
* Redacción de mensajes de commit estructurados (Conventional Commits).
* Actualización y mantenimiento de la documentación en la carpeta `docs/`.
* Publicación y sincronización con el repositorio remoto (`git push`).

---

## 📋 Reglas del Flujo de Trabajo

### 1. Nomenclatura de Ramas
* `feature/<nombre-feature>`: Para desarrollo de código, algoritmos o simulación.
* `docs/<nombre-doc>`: Para agregar o modificar documentación técnica.
* `fix/<nombre-bug>`: Para corrección de errores en código o modelos.

### 2. Estándar de Commits (Conventional Commits)
Usar el formato: `<tipo>(<alcance>): <descripción corta en presente/imperativo>`

Tipos permitidos:
* `feat`: Nueva funcionalidad o módulo.
* `docs`: Cambios o adiciones a la documentación.
* `fix`: Corrección de errores.
* `refactor`: Reestructuración de código sin cambiar comportamiento.
* `style`: Formato, espacios o limpieza de código.

*Ejemplo:*
```bash
git commit -m "docs(hitl): agregar definicion de objetivos y contexto en proyecto_contexto_hitl.md"