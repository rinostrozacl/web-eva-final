# HU-OPC-02: Propina al cerrar

## Obligatoriedad

Opcional (bonus)

## Historia de usuario

**Como** mozo  
**Quiero** agregar propina opcional al cerrar la cuenta  
**Para** registrar el total final a cobrar

## Criterios de aceptación

- [ ] Dado total de comanda, cuando agrego propina, entonces el total final incluye propina.
- [ ] Dado cierre, entonces se guarda monto con propina.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Comanda con total conocido.
2. Agregar propina.
3. Verificar total final y cierre.
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
5. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento).
