# HU-OPC-02: Asignar profesionales a servicios

## Obligatoriedad

Opcional (bonus)

## Historia de usuario

**Como** administrador  
**Quiero** asignar profesionales o recursos a cada servicio  
**Para** gestionar quién atiende cada cita

## Criterios de aceptación

- [ ] Dado profesionales registrados, cuando asigno uno a un servicio, entonces la asignación persiste.
- [ ] Dado una reserva, cuando se crea, entonces puede asociarse al profesional asignado (si el grupo lo modeló así).

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Crear o seleccionar profesional/recurso.
2. Asignarlo a un servicio desde la web.
3. Verificar persistencia y visualización en reserva o agenda.
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
5. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento).
