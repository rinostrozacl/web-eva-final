# HU-OPC-01: Ordenar resultados de búsqueda

## Obligatoriedad

Opcional (bonus)

## Historia de usuario

**Como** pasajero  
**Quiero** ordenar resultados por precio o horario  
**Para** comparar opciones como en un comparador

## Criterios de aceptación

- [ ] Dado múltiples viajes en búsqueda, cuando ordeno por precio, entonces el listado se reordena correctamente.
- [ ] Dado orden por horario, cuando aplico, entonces los viajes quedan ordenados por hora de salida.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Buscar ruta con varios viajes.
2. Aplicar orden por precio y verificar.
3. Aplicar orden por horario y verificar.
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
5. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento).
