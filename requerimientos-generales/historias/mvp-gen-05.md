# MVP-GEN-05: Login con JWT

## Obligatoriedad

Obligatoria

## Historia de usuario

**Como** usuario registrado  
**Quiero** iniciar sesión con JWT  
**Para** usar funciones protegidas del sistema

## Criterios de aceptación

- [ ] Dado un usuario registrado, cuando ingreso email y contraseña correctos, entonces accedo al sistema.
- [ ] Dado una ruta protegida, cuando llamo sin token, entonces recibo 401.
- [ ] Dado una ruta protegida, cuando llamo con token válido, entonces la operación se permite.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. En producción, ir a login e ingresar usuario de prueba.
2. Confirmar acceso a área autenticada (menú, dashboard o similar).
3. Opcional API: `GET` a ruta protegida sin `Authorization` → 401.
4. Opcional API: misma ruta con `Bearer <token>` → 200 o 201 según caso.
5. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
