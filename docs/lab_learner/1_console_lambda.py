class ConsolaAWS:
  def __init__(self, region_name):
    self.region_name = region_name
    # Inicializar otros recursos de AWS necesarios (si los hay)

  def crear_funcion_lambda(self, nombre_funcion, codigo_funcion, handler_funcion):
    # Implementar la lógica para crear la función Lambda en AWS
    """Un kit de desarrollo de software (SDK) es un conjunto de herramientas
     de desarrollo específicas de la plataforma para desarrolladores ."""
    # Utilizar el SDK de AWS para Boto3 o la API de AWS correspondiente
    print(f"Creando función Lambda: {nombre_funcion} en la región: {self.region_name}")
    # Simular la creación exitosa de la función Lambda
    return {
      "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:" + nombre_funcion
    }

  def invocar_funcion_lambda(self, nombre_funcion, evento):
    # Implementar la lógica para invocar la función Lambda en AWS
    # Utilizar el SDK de AWS para Boto3 o la API de AWS correspondiente
    print(f"Invocando función Lambda: {nombre_funcion} con evento: {evento}")
    # Simular la invocación exitosa de la función Lambda y devolver la respuesta
    return {
      "Salida": "Hola, mundo!"
    }

  def handler_lambda(event, context):
    # Procesar el evento (si es necesario)
    nombre = event.get("nombre", "Mundo") # Indent this line and subsequent lines within the function
    mensaje_saludo = f"¡Hola, {nombre}!"

    # Devolver un mensaje de saludo
    return {
      "mensaje": mensaje_saludo
    } 
# Simulando la consola de AWS
consola_aws = ConsolaAWS("us-east-1")

# Crear la función Lambda
funcion_lambda = consola_aws.crear_funcion_lambda(
    nombre_funcion="funcion-saludo",
    codigo_funcion="""
def handler_lambda(event, context):
  # ... (código de la función handler_lambda)
""",
    handler_funcion="handler_lambda"
)

# Invocar la función Lambda
evento_json = '{"nombre": "Juan"}'
respuesta_lambda = consola_aws.invocar_funcion_lambda(nombre_funcion="funcion_saludo", evento=evento_json)

# Mostrar la respuesta de la función Lambda
print(f"Respuesta de la función Lambda: {respuesta_lambda}")