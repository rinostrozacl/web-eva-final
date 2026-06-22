# MVP-GEN-04: Registro de usuario

## Obligatoriedad

Obligatoria

## Historia de usuario

**Como** usuario nuevo  
**Quiero** registrarme desde la web  
**Para** acceder al sistema

## Criterios de aceptación

- [ ] Dado un visitante, cuando completo el formulario de registro y envío, entonces recibo confirmación de éxito.
- [ ] Dado un usuario registrado, cuando consulto la API o BD, entonces el usuario existe persistido.
- [ ] Dado credenciales inválidas (email vacío o password corto), cuando intento registrarme, entonces veo error claro.

## Requiere interfaz web

Sí

## Procedimiento de verificación (corrector)

1. Ir a la URL pública del frontend.
2. Abrir pantalla de registro.
3. Crear usuario de prueba con email y contraseña válidos.
4. Confirmar mensaje de éxito o redirección.
5. Iniciar sesión con ese usuario (o verificar en API `POST /register` + login).
6. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario.
