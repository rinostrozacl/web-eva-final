# MVP-GEN-02: Variables de entorno documentadas

## Obligatoriedad

Obligatoria

## Historia de usuario

**Como** desarrollador  
**Quiero** un archivo `.env.example` sin secretos reales  
**Para** configurar el entorno sin exponer credenciales

## Criterios de aceptación

- [ ] Dado el repositorio, cuando busco `.env.example`, entonces existe y lista las variables necesarias.
- [ ] Dado `.env.example`, cuando reviso el contenido, entonces no contiene passwords ni JWT secrets reales.
- [ ] Dado el README, cuando consulto configuración, entonces explica cómo copiar `.env.example` a `.env`.

## Requiere interfaz web

No

## Procedimiento de verificación (corrector)

1. Abrir `.env.example` en el repositorio.
2. Verificar variables documentadas (DB, JWT, puerto, URL API para front).
3. Confirmar que los valores son placeholders, no secretos de producción.
4. Confirmar `.env` en `.gitignore`.
5. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
