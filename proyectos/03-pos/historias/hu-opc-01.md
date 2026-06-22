# HU-OPC-01: Boleta simulada

## Obligatoriedad

Opcional (bonus)

## Historia de usuario

**Como** cajero  
**Quiero** emitir un documento de venta simulado con número correlativo  
**Para** entregar comprobante al cliente

## Criterios de aceptación

- [ ] Dado venta confirmada, cuando solicito comprobante, entonces veo boleta con número único correlativo.
- [ ] Dado la boleta, entonces lista ítems y total.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Confirmar una venta.
2. Abrir o generar comprobante/boleta.
3. Verificar número correlativo e ítems.
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
5. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento).
