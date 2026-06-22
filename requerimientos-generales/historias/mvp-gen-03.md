# MVP-GEN-03: Base de datos y modelos

## Obligatoriedad

Obligatoria

## Historia de usuario

**Como** equipo  
**Quiero** al menos 2 modelos Sequelize con migraciones en PostgreSQL  
**Para** persistir el dominio del sistema

## Criterios de aceptación

- [ ] Dado el proyecto, cuando ejecuto migraciones, entonces se crean tablas en PostgreSQL.
- [ ] Dado la base de datos, cuando inspecciono esquema, entonces hay al menos 2 tablas del dominio.
- [ ] Dado los modelos, cuando reviso código, entonces están definidos en Sequelize.

## Requiere interfaz web

No

## Procedimiento de verificación (corrector)

1. Revisar carpeta `migrations/` o equivalente en el repo.
2. Verificar al menos 2 modelos/entidades del dominio (no solo `User`).
3. Opcional: conectar a BD de producción o evidencia en README de tablas creadas.
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
