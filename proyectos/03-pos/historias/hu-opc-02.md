# HU-OPC-02: Alertas de stock bajo

## Obligatoriedad

Opcional (bonus)

## Historia de usuario

**Como** administrador  
**Quiero** ver alertas de productos con stock bajo umbral  
**Para** reponer inventario a tiempo

## Criterios de aceptación

- [ ] Dado umbral configurado, cuando stock <= umbral, entonces el producto aparece en alertas.
- [ ] Dado stock por encima del umbral, entonces no aparece en alertas.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Configurar umbral o usar default.
2. Bajar stock de producto bajo umbral.
3. Verificar alerta en panel.
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
5. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento).
