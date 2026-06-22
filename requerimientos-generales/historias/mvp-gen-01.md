# MVP-GEN-01: Repositorio ejecutable

## Obligatoriedad

Obligatoria

## Historia de usuario

**Como** desarrollador  
**Quiero** un repositorio con estructura `client/` + API + README ejecutable  
**Para** que cualquiera pueda clonar, instalar y levantar el proyecto

## Criterios de aceptación

- [ ] Dado el repositorio entregado, cuando sigo el README (clone, install, run), entonces la API y el front levantan en local sin errores críticos.
- [ ] Dado el repositorio, cuando reviso la estructura, entonces existen carpetas `client/` y servidor API con migraciones o modelos visibles.
- [ ] Dado el README, cuando lo leo, entonces describe stack, instalación, variables y ejecución local.

## Requiere interfaz web

No

## Procedimiento de verificación (corrector)

1. Clonar el repositorio del grupo desde la URL entregada.
2. Seguir el README: instalar dependencias y levantar API + front en local (o verificar evidencia en README de que el corrector ya lo hizo).
3. Confirmar estructura `client/` + backend + `.gitignore` presente.
4. Confirmar que no hay secretos reales en el repo.
5. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
