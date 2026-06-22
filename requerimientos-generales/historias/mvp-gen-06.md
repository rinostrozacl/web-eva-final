# MVP-GEN-06: Frontend integrado al dominio

## Obligatoriedad

Obligatoria

## Historia de usuario

**Como** usuario  
**Quiero** operar el dominio desde pantallas web conectadas a la API  
**Para** no depender solo de Postman para el flujo principal

## Criterios de aceptación

- [ ] Dado usuario autenticado, cuando uso al menos 3 pantallas de dominio, entonces los datos vienen de la API (no mock estático).
- [ ] Dado una acción en web (crear, listar, transacción), cuando se completa, entonces persiste y se refleja al recargar.
- [ ] Dado error de API (409, 400), cuando ocurre en UI, entonces el usuario ve feedback legible.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Navegar al menos 3 pantallas del dominio (ej. listado, formulario, detalle o transacción).
2. Ejecutar una operación de escritura (crear reserva, venta, anuncio, etc.) desde la web.
3. Recargar página y verificar que el dato persiste.
4. Confirmar que las pantallas consumen la API desplegada (Network tab o URL API en config).
5. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
