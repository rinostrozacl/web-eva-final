# HU-OPC-01: Confirmación visual de reserva

## Obligatoriedad

Opcional (bonus)

## Historia de usuario

**Como** cliente  
**Quiero** recibir confirmación visual con resumen de la cita (servicio, fecha, hora, precio)  
**Para** tener evidencia de mi reserva

## Criterios de aceptación

- [ ] Dado una reserva confirmada, cuando termino el flujo, entonces veo pantalla o modal con resumen completo.
- [ ] Dado el resumen, cuando lo leo, entonces incluye servicio, fecha, hora y precio.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Completar una reserva en producción.
2. Verificar pantalla de confirmación con los 4 datos.
3. Marcar +5 pts si cumple; 0 si no implementado.
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
5. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento).
