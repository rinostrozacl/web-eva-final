#!/usr/bin/env python3
"""Genera historias de usuario para trabajo grupal MVP."""
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

MVP_GEN = [
    ("mvp-gen-01", "Repositorio ejecutable", "desarrollador",
     "un repositorio con estructura `client/` + API + README ejecutable",
     "que cualquiera pueda clonar, instalar y levantar el proyecto",
     "No",
     [
         "Dado el repositorio entregado, cuando sigo el README (clone, install, run), entonces la API y el front levantan en local sin errores críticos.",
         "Dado el repositorio, cuando reviso la estructura, entonces existen carpetas `client/` y servidor API con migraciones o modelos visibles.",
         "Dado el README, cuando lo leo, entonces describe stack, instalación, variables y ejecución local.",
     ],
     [
         "Clonar el repositorio del grupo desde la URL entregada.",
         "Seguir el README: instalar dependencias y levantar API + front en local (o verificar evidencia en README de que el corrector ya lo hizo).",
         "Confirmar estructura `client/` + backend + `.gitignore` presente.",
         "Confirmar que no hay secretos reales en el repo.",
     ]),
    ("mvp-gen-02", "Variables de entorno documentadas", "desarrollador",
     "un archivo `.env.example` sin secretos reales",
     "configurar el entorno sin exponer credenciales",
     "No",
     [
         "Dado el repositorio, cuando busco `.env.example`, entonces existe y lista las variables necesarias.",
         "Dado `.env.example`, cuando reviso el contenido, entonces no contiene passwords ni JWT secrets reales.",
         "Dado el README, cuando consulto configuración, entonces explica cómo copiar `.env.example` a `.env`.",
     ],
     [
         "Abrir `.env.example` en el repositorio.",
         "Verificar variables documentadas (DB, JWT, puerto, URL API para front).",
         "Confirmar que los valores son placeholders, no secretos de producción.",
         "Confirmar `.env` en `.gitignore`.",
     ]),
    ("mvp-gen-03", "Base de datos y modelos", "equipo",
     "al menos 2 modelos Sequelize con migraciones en PostgreSQL",
     "persistir el dominio del sistema",
     "No",
     [
         "Dado el proyecto, cuando ejecuto migraciones, entonces se crean tablas en PostgreSQL.",
         "Dado la base de datos, cuando inspecciono esquema, entonces hay al menos 2 tablas del dominio.",
         "Dado los modelos, cuando reviso código, entonces están definidos en Sequelize.",
     ],
     [
         "Revisar carpeta `migrations/` o equivalente en el repo.",
         "Verificar al menos 2 modelos/entidades del dominio (no solo `User`).",
         "Opcional: conectar a BD de producción o evidencia en README de tablas creadas.",
     ]),
    ("mvp-gen-04", "Registro de usuario", "usuario nuevo",
     "registrarme desde la web",
     "acceder al sistema",
     "Sí",
     [
         "Dado un visitante, cuando completo el formulario de registro y envío, entonces recibo confirmación de éxito.",
         "Dado un usuario registrado, cuando consulto la API o BD, entonces el usuario existe persistido.",
         "Dado credenciales inválidas (email vacío o password corto), cuando intento registrarme, entonces veo error claro.",
     ],
     [
         "Ir a la URL pública del frontend.",
         "Abrir pantalla de registro.",
         "Crear usuario de prueba con email y contraseña válidos.",
         "Confirmar mensaje de éxito o redirección.",
         "Iniciar sesión con ese usuario (o verificar en API `POST /register` + login).",
     ]),
    ("mvp-gen-05", "Login con JWT", "usuario registrado",
     "iniciar sesión con JWT",
     "usar funciones protegidas del sistema",
     "Sí",
     [
         "Dado un usuario registrado, cuando ingreso email y contraseña correctos, entonces accedo al sistema.",
         "Dado una ruta protegida, cuando llamo sin token, entonces recibo 401.",
         "Dado una ruta protegida, cuando llamo con token válido, entonces la operación se permite.",
     ],
     [
         "En producción, ir a login e ingresar usuario de prueba.",
         "Confirmar acceso a área autenticada (menú, dashboard o similar).",
         "Opcional API: `GET` a ruta protegida sin `Authorization` → 401.",
         "Opcional API: misma ruta con `Bearer <token>` → 200 o 201 según caso.",
     ]),
    ("mvp-gen-06", "Frontend integrado al dominio", "usuario",
     "operar el dominio desde pantallas web conectadas a la API",
     "no depender solo de Postman para el flujo principal",
     "Sí",
     [
         "Dado usuario autenticado, cuando uso al menos 3 pantallas de dominio, entonces los datos vienen de la API (no mock estático).",
         "Dado una acción en web (crear, listar, transacción), cuando se completa, entonces persiste y se refleja al recargar.",
         "Dado error de API (409, 400), cuando ocurre en UI, entonces el usuario ve feedback legible.",
     ],
     [
         "Navegar al menos 3 pantallas del dominio (ej. listado, formulario, detalle o transacción).",
         "Ejecutar una operación de escritura (crear reserva, venta, anuncio, etc.) desde la web.",
         "Recargar página y verificar que el dato persiste.",
         "Confirmar que las pantallas consumen la API desplegada (Network tab o URL API en config).",
     ]),
    ("mvp-gen-07", "Deploy público", "corrector",
     "acceder al sistema en URLs públicas",
     "evaluar sin instalar nada en local",
     "Parcial",
     [
         "Dado las URLs entregadas, cuando abro el frontend en el navegador, entonces carga la aplicación.",
         "Dado el frontend en producción, cuando ejecuto flujo login + una HU de dominio, entonces funciona contra API pública.",
         "Dado la URL de API, cuando hago health check o login, entonces responde (no timeout ni 502).",
     ],
     [
         "Abrir URL del frontend entregada en matriz/README.",
         "Abrir URL de la API (health o login).",
         "Ejecutar login y al menos una operación de dominio en producción.",
         "Si API o front no responden: marcar penalización según rúbrica (-20 pts deploy).",
     ]),
]

PROJECTS = {
    "01-reservas": {
        "title": "Sistema de reservas",
        "ref": "Reservio",
        "entities": "Servicio, Reserva, Disponibilidad",
        "hus": [
            ("hu-01", "Definir servicios reservables", "administrador", "definir servicios con nombre, duración y precio", "ofrecer citas reservables a los clientes", "Parcial",
             ["Dado el modelo de datos, cuando reviso API o BD, entonces existe entidad Servicio con nombre, duración y precio.",
              "Dado un servicio creado vía API o seed, cuando consulto el recurso, entonces devuelve los campos definidos."],
             ["Revisar modelo/migración Servicio en repo o crear uno vía API.",
              "Verificar campos mínimos: nombre, duración (min), precio.",
              "Confirmar persistencia en PostgreSQL."]),
            ("hu-02", "Gestionar servicios desde la web", "administrador", "crear, editar y eliminar servicios desde la web", "mantener mi catálogo actualizado", "Sí",
             ["Dado usuario autenticado como admin, cuando creo un servicio desde web, entonces aparece en el listado.",
              "Dado un servicio existente, cuando lo edito, entonces los cambios se guardan.",
              "Dado un servicio sin reservas activas (o según regla del grupo), cuando lo elimino, entonces desaparece del listado."],
             ["Login en producción.",
              "Ir a gestión de servicios.",
              "Crear servicio; verificar en listado.",
              "Editar nombre o precio; guardar y verificar.",
              "Eliminar o desactivar un servicio de prueba; verificar que ya no aparece (o marca inactivo)."]),
            ("hu-03", "Configurar horarios disponibles", "administrador", "configurar horarios disponibles por día", "que los clientes solo reserven en franjas válidas", "Sí",
             ["Dado un día de la semana, cuando configuro franjas horarias, entonces quedan guardadas.",
              "Dado horarios configurados, cuando un cliente reserva, entonces solo ve slots dentro de esas franjas."],
             ["Login como administrador.",
              "Configurar disponibilidad para al menos un día (ej. lun 09:00–18:00 con slots de 30 min).",
              "Guardar y verificar persistencia.",
              "Como cliente, abrir reserva y confirmar que solo aparecen horarios válidos."]),
            ("hu-04", "Reservar una cita", "cliente", "reservar una cita eligiendo servicio, fecha y hora", "agendar mi atención", "Sí",
             ["Dado servicios y horarios disponibles, cuando elijo servicio, fecha y hora y confirmo, entonces la reserva queda creada.",
              "Dado la reserva creada, cuando consulto mis reservas o agenda, entonces aparece con los datos correctos."],
             ["Login o flujo de cliente.",
              "Elegir servicio, fecha y hora disponible.",
              "Confirmar reserva.",
              "Ver mensaje de éxito y reserva visible en listado o agenda."]),
            ("hu-05", "Listar reservas por fecha", "administrador", "ver las reservas filtradas por fecha", "organizar la agenda del día", "Sí",
             ["Dado reservas existentes, cuando filtro por una fecha, entonces solo veo reservas de ese día.",
              "Dado el filtro, cuando cambio la fecha, entonces el listado se actualiza."],
             ["Login como administrador.",
              "Ir a listado de reservas.",
              "Seleccionar fecha con reservas conocidas.",
              "Verificar que solo aparecen reservas de esa fecha."]),
            ("hu-06", "Cancelar reserva", "cliente", "cancelar una reserva existente", "liberar el horario si no puedo asistir", "Sí",
             ["Dado una reserva activa propia, cuando cancelo, entonces el estado cambia a cancelada.",
              "Dado la reserva cancelada, cuando otro cliente busca ese slot, entonces el horario vuelve a estar disponible."],
             ["Crear o usar reserva activa de prueba.",
              "Cancelar desde la web.",
              "Confirmar estado cancelado en UI.",
              "Verificar que el slot queda disponible para nueva reserva."]),
            ("hu-07", "Evitar doble reserva en mismo slot", "sistema", "impedir dos reservas en el mismo slot", "evitar sobreventa de horarios", "Sí",
             ["Dado un slot ya reservado, cuando otro usuario intenta reservar el mismo slot, entonces la operación falla con error visible.",
              "Dado el conflicto, cuando ocurre en API, entonces responde 409 o 400 con mensaje claro."],
             ["Reservar un slot específico (servicio + fecha + hora).",
              "Con otro usuario o sesión, intentar reservar el mismo slot.",
              "Verificar mensaje de error en pantalla (no permite confirmar).",
              "Opcional: API devuelve 409."]),
            ("hu-08", "Vista agenda del día", "administrador", "una vista de agenda del día con todas las citas", "visualizar la jornada de un vistazo", "Sí",
             ["Dado reservas en un día, cuando abro la agenda de ese día, entonces veo todas las citas ordenadas por hora.",
              "Dado la vista agenda, cuando selecciono otro día, entonces se actualiza el contenido."],
             ["Login como administrador.",
              "Abrir vista agenda o calendario del día.",
              "Seleccionar fecha con reservas.",
              "Verificar que muestra servicio, hora y cliente (o identificador) por cita."]),
        ],
        "opc": [
            ("hu-opc-01", "Confirmación visual de reserva", "cliente", "recibir confirmación visual con resumen de la cita (servicio, fecha, hora, precio)", "tener evidencia de mi reserva", "Sí",
             ["Dado una reserva confirmada, cuando termino el flujo, entonces veo pantalla o modal con resumen completo.",
              "Dado el resumen, cuando lo leo, entonces incluye servicio, fecha, hora y precio."],
             ["Completar una reserva en producción.",
              "Verificar pantalla de confirmación con los 4 datos.",
              "Marcar +5 pts si cumple; 0 si no implementado."]),
            ("hu-opc-02", "Asignar profesionales a servicios", "administrador", "asignar profesionales o recursos a cada servicio", "gestionar quién atiende cada cita", "Sí",
             ["Dado profesionales registrados, cuando asigno uno a un servicio, entonces la asignación persiste.",
              "Dado una reserva, cuando se crea, entonces puede asociarse al profesional asignado (si el grupo lo modeló así)."],
             ["Crear o seleccionar profesional/recurso.",
              "Asignarlo a un servicio desde la web.",
              "Verificar persistencia y visualización en reserva o agenda."]),
        ],
    },
    "02-pasajes": {
        "title": "Venta de pasajes",
        "ref": "Recorrido.cl",
        "entities": "Viaje, Asiento, Pasaje",
        "hus": [
            ("hu-01", "Registrar viajes", "operador", "registrar viajes con origen, destino, fecha, hora y precio", "publicar oferta de transporte", "Parcial",
             ["Dado el modelo Viaje, cuando reviso campos, entonces incluye origen, destino, fecha/hora y precio.",
              "Dado un viaje creado, cuando consulto API, entonces persiste en BD."],
             ["Revisar modelo Viaje o crear vía API.",
              "Verificar campos obligatorios.",
              "Confirmar persistencia."]),
            ("hu-02", "Gestionar viajes desde la web", "operador", "crear, editar y eliminar viajes desde la web", "actualizar horarios y tarifas", "Sí",
             ["Dado operador autenticado, cuando creo viaje en web, entonces aparece en listado.",
              "Dado viaje existente, cuando edito precio u horario, entonces se guarda."],
             ["Login como operador.",
              "Crear viaje; verificar listado.",
              "Editar precio u horario; guardar y verificar."]),
            ("hu-03", "Buscar viajes", "pasajero", "buscar viajes por origen, destino y fecha", "encontrar opciones de viaje", "Sí",
             ["Dado viajes publicados, cuando busco por origen, destino y fecha, entonces veo resultados coincidentes.",
              "Dado criterios sin resultados, cuando busco, entonces veo mensaje de sin resultados."],
             ["Ir a búsqueda de viajes.",
              "Ingresar origen, destino y fecha con viajes conocidos.",
              "Verificar listado de resultados.",
              "Buscar fecha sin viajes y ver mensaje vacío."]),
            ("hu-04", "Ver asientos disponibles", "pasajero", "ver los asientos disponibles de un viaje", "elegir dónde sentarme", "Sí",
             ["Dado un viaje seleccionado, cuando abro selección de asientos, entonces veo mapa o lista con estado libre/ocupado.",
              "Dado asientos ocupados, cuando miro la UI, entonces no aparecen como seleccionables."],
             ["Seleccionar un viaje de la búsqueda.",
              "Abrir pantalla de asientos.",
              "Verificar que se distinguen disponibles vs ocupados."]),
            ("hu-05", "Comprar pasaje con asiento", "pasajero", "comprar un pasaje seleccionando asiento", "confirmar mi viaje", "Sí",
             ["Dado asiento libre, cuando selecciono y confirmo compra, entonces el pasaje queda registrado.",
              "Dado la compra, cuando consulto mis pasajes, entonces aparece el nuevo pasaje."],
             ["Seleccionar asiento libre.",
              "Confirmar compra (login si aplica).",
              "Ver confirmación y pasaje en «mis pasajes»."]),
            ("hu-06", "Bloquear asiento ya vendido", "sistema", "bloquear un asiento ya vendido", "no vender el mismo lugar dos veces", "Sí",
             ["Dado asiento vendido, cuando otro usuario intenta comprarlo, entonces la operación falla.",
              "Dado el intento en API, entonces responde 409 o equivalente."],
             ["Comprar un asiento específico.",
              "Con otra sesión, intentar comprar el mismo asiento.",
              "Verificar bloqueo en UI y/o 409 en API."]),
            ("hu-07", "Mis pasajes", "pasajero autenticado", "ver mis pasajes comprados", "consultar mis viajes", "Sí",
             ["Dado pasajes comprados por el usuario, cuando abro «mis pasajes», entonces veo listado con origen, destino, fecha y asiento.",
              "Dado usuario sin pasajes, cuando abro la sección, entonces veo estado vacío claro."],
             ["Login como pasajero con pasajes.",
              "Abrir «mis pasajes».",
              "Verificar datos del viaje y asiento."]),
            ("hu-08", "Comprobante de pasaje", "pasajero", "ver un comprobante con los datos del pasaje", "tener evidencia de la compra", "Sí",
             ["Dado un pasaje comprado, cuando abro comprobante o detalle, entonces veo origen, destino, fecha, asiento y precio.",
              "Dado el comprobante, cuando lo visualizo, entonces los datos coinciden con la compra."],
             ["Abrir detalle o comprobante de un pasaje.",
              "Verificar todos los campos requeridos."]),
        ],
        "opc": [
            ("hu-opc-01", "Ordenar resultados de búsqueda", "pasajero", "ordenar resultados por precio o horario", "comparar opciones como en un comparador", "Sí",
             ["Dado múltiples viajes en búsqueda, cuando ordeno por precio, entonces el listado se reordena correctamente.",
              "Dado orden por horario, cuando aplico, entonces los viajes quedan ordenados por hora de salida."],
             ["Buscar ruta con varios viajes.",
              "Aplicar orden por precio y verificar.",
              "Aplicar orden por horario y verificar."]),
            ("hu-opc-02", "Comprobante en PDF", "pasajero", "descargar o imprimir el comprobante en PDF", "llevar el pasaje sin conexión", "Sí",
             ["Dado pasaje comprado, cuando solicito PDF, entonces se genera o descarga archivo.",
              "Dado el PDF, cuando lo abro, entonces contiene datos del pasaje."],
             ["Comprar o usar pasaje existente.",
              "Clic en descargar/imprimir PDF.",
              "Abrir archivo y verificar contenido."]),
        ],
    },
    "03-pos": {
        "title": "Punto de venta (POS)",
        "ref": "Bsale",
        "entities": "Producto, Venta, LíneaVenta",
        "hus": [
            ("hu-01", "Registrar productos", "administrador", "registrar productos con nombre, precio y stock", "controlar el inventario", "Parcial",
             ["Dado modelo Producto, cuando reviso campos, entonces incluye nombre, precio y stock.",
              "Dado producto creado, entonces persiste en BD."],
             ["Revisar modelo o crear producto vía API/web.",
              "Verificar campos y persistencia."]),
            ("hu-02", "Gestionar productos desde la web", "administrador", "crear, editar y eliminar productos desde la web", "mantener el catálogo", "Sí",
             ["Dado admin autenticado, cuando CRUD producto en web, entonces cambios persisten en listado."],
             ["Login admin.",
              "Crear, editar y eliminar producto de prueba.",
              "Verificar listado actualizado."]),
            ("hu-03", "Pantalla POS con catálogo", "cajero", "una pantalla POS con el catálogo de productos visible", "vender rápidamente", "Sí",
             ["Dado productos en catálogo, cuando abro POS, entonces veo productos con nombre y precio.",
              "Dado la pantalla POS, cuando navego, entonces puedo seleccionar productos."],
             ["Abrir pantalla POS/mostrador.",
              "Verificar catálogo visible con precios."]),
            ("hu-04", "Carrito de venta", "cajero", "agregar productos a un carrito de venta", "armar el pedido del cliente", "Sí",
             ["Dado productos en catálogo, cuando agrego al carrito, entonces aparecen con cantidad y subtotal.",
              "Dado ítems en carrito, cuando modifico cantidad, entonces el subtotal se actualiza."],
             ["Agregar 2 productos al carrito.",
              "Verificar cantidades y subtotales.",
              "Cambiar cantidad y ver recálculo."]),
            ("hu-05", "Confirmar venta con total", "cajero", "confirmar la venta con total calculado", "cerrar la transacción", "Sí",
             ["Dado carrito con ítems, cuando confirmo venta, entonces se registra con total = suma de líneas.",
              "Dado venta confirmada, entonces el carrito se vacía o muestra éxito."],
             ["Armar carrito con productos conocidos.",
              "Confirmar venta.",
              "Verificar total correcto y mensaje de éxito."]),
            ("hu-06", "Descontar stock al vender", "sistema", "descontar stock al confirmar una venta", "reflejar el inventario real", "Parcial",
             ["Dado producto con stock N, cuando vendo cantidad C, entonces stock pasa a N-C.",
              "Dado la venta, cuando consulto producto, entonces stock actualizado."],
             ["Anotar stock inicial de producto.",
              "Vender cantidad conocida.",
              "Verificar stock disminuido en catálogo o BD."]),
            ("hu-07", "No vender sin stock", "sistema", "impedir vender productos sin stock", "no comprometer ventas imposibles", "Sí",
             ["Dado producto con stock 0, cuando intento agregarlo al carrito o confirmar, entonces la operación falla con mensaje claro."],
             ["Poner producto en stock 0.",
              "Intentar vender desde POS.",
              "Verificar bloqueo y mensaje de error."]),
            ("hu-08", "Listado ventas del día", "cajero", "listar las ventas del día con filtro por fecha", "revisar el movimiento", "Sí",
             ["Dado ventas registradas, cuando filtro por fecha de hoy, entonces veo ventas de ese día con total.",
              "Dado otra fecha, cuando filtro, entonces el listado cambia."],
             ["Registrar venta de prueba.",
              "Abrir listado de ventas.",
              "Filtrar por fecha y verificar venta visible con monto."]),
        ],
        "opc": [
            ("hu-opc-01", "Boleta simulada", "cajero", "emitir un documento de venta simulado con número correlativo", "entregar comprobante al cliente", "Sí",
             ["Dado venta confirmada, cuando solicito comprobante, entonces veo boleta con número único correlativo.",
              "Dado la boleta, entonces lista ítems y total."],
             ["Confirmar una venta.",
              "Abrir o generar comprobante/boleta.",
              "Verificar número correlativo e ítems."]),
            ("hu-opc-02", "Alertas de stock bajo", "administrador", "ver alertas de productos con stock bajo umbral", "reponer inventario a tiempo", "Sí",
             ["Dado umbral configurado, cuando stock <= umbral, entonces el producto aparece en alertas.",
              "Dado stock por encima del umbral, entonces no aparece en alertas."],
             ["Configurar umbral o usar default.",
              "Bajar stock de producto bajo umbral.",
              "Verificar alerta en panel."]),
        ],
    },
    "04-restaurante": {
        "title": "Sistema para restaurantes",
        "ref": "Fudo",
        "entities": "Mesa, Ítem menú, Comanda",
        "hus": [
            ("hu-01", "Registrar mesas", "administrador", "registrar mesas con número, capacidad y estado", "organizar el salón", "Parcial",
             ["Dado modelo Mesa, entonces incluye número, capacidad y estado (libre/ocupada)."],
             ["Revisar modelo Mesa o crear vía web.",
              "Verificar campos y persistencia."]),
            ("hu-02", "Gestionar mesas y menú", "administrador", "gestionar mesas e ítems del menú desde la web", "mantener la carta y el salón actualizados", "Sí",
             ["Dado admin, cuando CRUD mesa e ítem menú, entonces cambios persisten."],
             ["Crear/editar mesa e ítem de menú.",
              "Verificar en listados."]),
            ("hu-03", "Vista salón", "mozo", "ver qué mesas están libres u ocupadas", "atender al salón", "Sí",
             ["Dado mesas en distintos estados, cuando abro vista salón, entonces se distinguen libres vs ocupadas."],
             ["Abrir vista salón.",
              "Ocupar una mesa y verificar cambio visual.",
              "Liberar mesa y verificar estado libre."]),
            ("hu-04", "Abrir comanda", "mozo", "abrir una comanda en una mesa libre", "tomar el pedido", "Sí",
             ["Dado mesa libre, cuando abro comanda, entonces la mesa pasa a ocupada y existe comanda abierta."],
             ["Seleccionar mesa libre.",
              "Abrir comanda.",
              "Verificar mesa ocupada y comanda activa."]),
            ("hu-05", "Agregar ítems a comanda", "mozo", "agregar ítems del menú a la comanda", "registrar lo pedido", "Sí",
             ["Dado comanda abierta, cuando agrego ítems, entonces aparecen con cantidad y subtotal.",
              "Dado varios ítems, entonces el subtotal parcial se actualiza."],
             ["Abrir comanda.",
              "Agregar 2 ítems del menú.",
              "Verificar líneas y subtotales."]),
            ("hu-06", "Cerrar comanda y liberar mesa", "mozo", "cerrar la comanda y liberar la mesa", "atender nuevos clientes", "Sí",
             ["Dado comanda con ítems, cuando cierro comanda, entonces comanda queda cerrada y mesa libre."],
             ["Comanda con ítems.",
              "Cerrar comanda.",
              "Verificar mesa libre en vista salón."]),
            ("hu-07", "Total de cuenta", "mozo", "ver el total de la cuenta antes de cerrar", "cobrar el monto correcto", "Sí",
             ["Dado ítems en comanda, cuando veo total, entonces coincide con suma de precio × cantidad."],
             ["Agregar ítems con precios conocidos.",
              "Verificar total mostrado antes de cerrar.",
              "Comparar con suma manual."]),
            ("hu-08", "No liberar mesa con comanda abierta", "sistema", "impedir liberar una mesa con comanda abierta sin cerrar", "no perder pedidos pendientes", "Sí",
             ["Dado comanda abierta con ítems, cuando intento liberar mesa sin cerrar, entonces la operación falla o exige cerrar primero."],
             ["Mesa con comanda abierta.",
              "Intentar liberar sin cerrar.",
              "Verificar bloqueo o flujo que exige cierre."]),
        ],
        "opc": [
            ("hu-opc-01", "Vista cocina", "cocina", "ver ítems pendientes y marcarlos como en preparación o listo", "coordinar con el salón", "Sí",
             ["Dado ítems pedidos, cuando abro vista cocina, entonces veo pendientes.",
              "Dado ítem, cuando cambio estado a listo, entonces se refleja en cocina y/o mozo."],
             ["Pedir ítems en comanda.",
              "Abrir vista cocina.",
              "Cambiar estado de ítem y verificar."]),
            ("hu-opc-02", "Propina al cerrar", "mozo", "agregar propina opcional al cerrar la cuenta", "registrar el total final a cobrar", "Sí",
             ["Dado total de comanda, cuando agrego propina, entonces el total final incluye propina.",
              "Dado cierre, entonces se guarda monto con propina."],
             ["Comanda con total conocido.",
              "Agregar propina.",
              "Verificar total final y cierre."]),
        ],
    },
    "05-autos": {
        "title": "Anuncios de automóviles",
        "ref": "Chileautos",
        "entities": "Anuncio",
        "hus": [
            ("hu-01", "Modelar anuncios", "vendedor", "que el sistema almacene anuncios con marca, modelo, año, precio y kilometraje", "describir mi vehículo", "Parcial",
             ["Dado modelo Anuncio, entonces incluye marca, modelo, año, precio, km y estado."],
             ["Revisar modelo Anuncio.",
              "Verificar campos mínimos."]),
            ("hu-02", "Publicar anuncio", "vendedor autenticado", "publicar un anuncio desde la web", "ofrecer mi auto", "Sí",
             ["Dado usuario autenticado, cuando completo formulario y guardo, entonces el anuncio queda publicado.",
              "Dado anuncio publicado, entonces aparece en listado público."],
             ["Login como vendedor.",
              "Ir a publicar anuncio.",
              "Completar marca, modelo, año, precio, km; guardar.",
              "Ver confirmación y anuncio en listado."]),
            ("hu-03", "Listado público", "comprador", "ver el listado de anuncios activos", "explorar opciones", "Sí",
             ["Dado anuncios activos, cuando abro listado sin login, entonces veo tarjetas o tabla con datos básicos."],
             ["Abrir URL pública sin login.",
              "Ver listado con al menos un anuncio activo."]),
            ("hu-04", "Detalle de anuncio", "comprador", "ver el detalle de un anuncio", "evaluar un vehículo", "Sí",
             ["Dado anuncio en listado, cuando abro detalle, entonces veo todos los campos del vehículo."],
             ["Clic en anuncio del listado.",
              "Verificar detalle completo."]),
            ("hu-05", "Filtrar anuncios", "comprador", "filtrar por marca y rango de precio", "acotar la búsqueda", "Sí",
             ["Dado anuncios variados, cuando filtro por marca, entonces solo veo esa marca.",
              "Dado rango de precio, cuando aplico filtro, entonces solo veo anuncios dentro del rango."],
             ["Aplicar filtro marca.",
              "Aplicar filtro precio min/max.",
              "Verificar resultados coherentes."]),
            ("hu-06", "Editar anuncio propio", "vendedor", "editar mis anuncios publicados", "corregir o actualizar datos", "Sí",
             ["Dado mi anuncio, cuando edito precio o km y guardo, entonces los cambios persisten."],
             ["Login como dueño.",
              "Editar anuncio propio.",
              "Verificar cambios en listado y detalle."]),
            ("hu-07", "Marcar como vendido", "vendedor", "marcar un anuncio como vendido", "retirarlo del listado activo", "Sí",
             ["Dado mi anuncio activo, cuando marco vendido, entonces deja de aparecer en listado activo."],
             ["Marcar anuncio como vendido.",
              "Verificar que no aparece en listado público activo."]),
            ("hu-08", "Solo el dueño edita", "sistema", "que solo el dueño pueda editar o eliminar su anuncio", "proteger publicaciones ajenas", "Sí",
             ["Dado anuncio de otro usuario, cuando intento editar o eliminar, entonces recibo 403 o UI bloqueada.",
              "Dado mi anuncio, cuando edito, entonces sí se permite."],
             ["Login usuario A; crear anuncio.",
              "Login usuario B; intentar editar anuncio de A.",
              "Verificar bloqueo.",
              "Usuario A sí puede editar el suyo."]),
        ],
        "opc": [
            ("hu-opc-01", "Fotos en anuncio", "vendedor", "agregar una o más fotos (URL) al anuncio", "mostrar el estado del vehículo", "Sí",
             ["Dado anuncio, cuando agrego URL de foto, entonces se muestra en detalle y/o listado."],
             ["Editar o crear anuncio con URL de imagen.",
              "Verificar que la imagen se renderiza."]),
            ("hu-opc-02", "Contactar vendedor", "comprador", "enviar un mensaje de contacto al vendedor desde el detalle", "consultar por el auto", "Sí",
             ["Dado detalle de anuncio, cuando envío mensaje, entonces el vendedor recibe o queda registrado el contacto.",
              "Dado mensaje enviado, entonces veo confirmación."],
             ["Abrir detalle como comprador.",
              "Enviar mensaje de contacto.",
              "Verificar confirmación y registro (bandeja vendedor o BD)."]),
        ],
    },
}


def render_hu(hu_id, title, role, quiero, para, web, criteria, steps, optional=False):
    opt_line = "Opcional (bonus)" if optional else "Obligatoria"
    crit = "\n".join(f"- [ ] {c}" for c in criteria)
    proc = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    proc += f"\n{len(steps)+1}. Marcar **cumple (2)** si todos los pasos se completan; **parcial (1)** si falta web donde se exige; **no cumple (0)** en caso contrario."
    if optional:
        proc += "\n" + f"{len(steps)+2}. Bonus: **+5 pts** si cumple; **0** si no implementado (sin descuento)."
    return f"""# {hu_id.upper().replace('-', '-')}: {title}

## Obligatoriedad

{opt_line}

## Historia de usuario

**Como** {role}  
**Quiero** {quiero}  
**Para** {para}

## Criterios de aceptación

{crit}

## Requiere interfaz web

{web}

## Procedimiento de verificación (corrector)

{proc}
"""


def write_mvp_gen():
    out = BASE / "requerimientos-generales" / "historias"
    out.mkdir(parents=True, exist_ok=True)
    for item in MVP_GEN:
        hu_id, title, role, quiero, para, web, criteria, steps = item
        path = out / f"{hu_id}.md"
        path.write_text(render_hu(hu_id.upper(), title, role, quiero, para, web, criteria, steps), encoding="utf-8")


def write_lista_gen():
    content = """# Historias generales — Trabajo grupal MVP

Todas las historias **MVP-GEN** son **obligatorias** para cualquier tema elegido.

| ID | Título | [WEB] |
|----|--------|-------|
| [MVP-GEN-01](historias/mvp-gen-01.md) | Repositorio ejecutable | No |
| [MVP-GEN-02](historias/mvp-gen-02.md) | Variables de entorno documentadas | No |
| [MVP-GEN-03](historias/mvp-gen-03.md) | Base de datos y modelos | No |
| [MVP-GEN-04](historias/mvp-gen-04.md) | Registro de usuario | Sí |
| [MVP-GEN-05](historias/mvp-gen-05.md) | Login con JWT | Sí |
| [MVP-GEN-06](historias/mvp-gen-06.md) | Frontend integrado al dominio | Sí |
| [MVP-GEN-07](historias/mvp-gen-07.md) | Deploy público | Parcial |

**Total generales:** 7 historias obligatorias.

Cada proyecto suma 8 HU de dominio + 2 opcionales → **15 obligatorias + 2 bonus** por grupo.
"""
    (BASE / "requerimientos-generales" / "lista-historias.md").write_text(content, encoding="utf-8")


def write_lista_project(slug, data):
    num = slug.split("-")[0]
    rows_ob = "\n".join(
        f"| [{h[0].upper()}](historias/{h[0]}.md) | {h[1]} | {h[5]} |"
        for h in data["hus"]
    )
    rows_op = "\n".join(
        f"| [{h[0].upper()}](historias/{h[0]}.md) | {h[1]} | {h[5]} | +5 |"
        for h in data["opc"]
    )
    content = f"""# Historias — {data['title']}

Proyecto **#{num}** · `{slug}` · Inspiración: {data['ref']}

## Historias generales (obligatorias)

Cumplir **MVP-GEN-01 … MVP-GEN-07**:

- [lista-historias.md](../../requerimientos-generales/lista-historias.md)

## Historias de dominio (obligatorias)

| ID | Título | [WEB] |
|----|--------|-------|
{rows_ob}

## Historias opcionales (bonus)

| ID | Título | [WEB] | Puntos |
|----|--------|-------|--------|
{rows_op}

**Entidades orientativas:** {data['entities']}

**Total grupo:** 7 MVP-GEN + 8 HU = **15 obligatorias** · hasta **+10 bonus** con opcionales.
"""
    (BASE / "proyectos" / slug / "lista-historias.md").write_text(content, encoding="utf-8")


def write_all_projects():
    for slug, data in PROJECTS.items():
        hist_dir = BASE / "proyectos" / slug / "historias"
        hist_dir.mkdir(parents=True, exist_ok=True)
        for hu in data["hus"]:
            hu_id, title, role, quiero, para, web, criteria, steps = hu
            (hist_dir / f"{hu_id}.md").write_text(
                render_hu(hu_id.upper(), title, role, quiero, para, web, criteria, steps), encoding="utf-8"
            )
        for hu in data["opc"]:
            hu_id, title, role, quiero, para, web, criteria, steps = hu
            (hist_dir / f"{hu_id}.md").write_text(
                render_hu(hu_id.upper(), title, role, quiero, para, web, criteria, steps, optional=True),
                encoding="utf-8",
            )
        write_lista_project(slug, data)


if __name__ == "__main__":
    write_mvp_gen()
    write_lista_gen()
    write_all_projects()
    print("OK")
