# MVP-GEN-07: Deploy público

## Obligatoriedad

Obligatoria

## Historia de usuario

**Como** corrector  
**Quiero** acceder al sistema en URLs públicas  
**Para** evaluar sin instalar nada en local

## Criterios de aceptación

- [ ] Dado las URLs entregadas, cuando abro el frontend en el navegador, entonces carga la aplicación.
- [ ] Dado el frontend en producción, cuando ejecuto flujo login + una HU de dominio, entonces funciona contra API pública.
- [ ] Dado la URL de API, cuando hago health check o login, entonces responde (no timeout ni 502).

## Requiere interfaz web

Parcial

## Procedimiento de verificación (corrector)

1. Abrir URL del frontend entregada en matriz/README.
2. Abrir URL de la API (health o login).
3. Ejecutar login y al menos una operación de dominio en producción.
4. Si API o front no responden: marcar penalización según rúbrica (-20 pts deploy).
5. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
