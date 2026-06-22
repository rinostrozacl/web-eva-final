# HU-OPC-02: Contactar vendedor

## Obligatoriedad

Opcional (bonus)

## Historia de usuario

**Como** comprador  
**Quiero** enviar un mensaje de contacto al vendedor desde el detalle  
**Para** consultar por el auto

## Criterios de aceptación

- [ ] Dado detalle de anuncio, cuando envío mensaje, entonces el vendedor recibe o queda registrado el contacto.
- [ ] Dado mensaje enviado, entonces veo confirmación.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Abrir detalle como comprador.
2. Enviar mensaje de contacto.
3. Verificar confirmación y registro (bandeja vendedor o BD).
4. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
5. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento).
