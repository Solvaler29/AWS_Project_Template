def handler_lambda(event, context):
    # Procesar el evento (si es necesario)
    nombre = event.get("nombre", "Mundo")
    mensaje_saludo = f"¡Hola, {nombre}!"

    # Devolver un mensaje de saludo
    return {
        "mensaje": mensaje_saludo
    }