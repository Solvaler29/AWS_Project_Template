import boto3
import json

# Configuración de la región de AWS
region_name = "us-east-1"

# Nombre de la función Lambda
nombre_funcion = "funcion_lambda_ejemplo"

# Código de la función Lambda (handler)
codigo_funcion = """
def handler_lambda(event, context):
  # Procesar el evento (si es necesario)
  nombre = event.get("nombre", "Mundo")
  mensaje_saludo = f"¡Hola, {nombre}!"

  # Devolver un mensaje de saludo
  return {
    "mensaje": mensaje_saludo
  }
"""

# Nombre del rol IAM para la función Lambda
nombre_rol_iam = "rol_lambda_basico"

# Simulando la creación del rol IAM (asumiendo que ya existe)
print(f"Simulando creación de rol IAM: {nombre_rol_iam}")
print("**Nota:** Se asume que el rol IAM ya existe y tiene los permisos necesarios.")

# Simulando la asociación del rol IAM a la función Lambda
print(f"Simulando asociación de rol IAM: {nombre_rol_iam} a la función Lambda: {nombre_funcion}")
print("**Nota:** Se asume que la asociación del rol se realiza correctamente.")

# Simulando la creación de la función Lambda
print(f"Simulando creación de función Lambda: {nombre_funcion} en la región: {region_name}")
respuesta_creacion = {
  "FunctionArn": f"arn:aws:lambda:{region_name}:123456789012:function/{nombre_funcion}",
  "Message": "Función Lambda creada exitosamente."
}

# Verificando la respuesta de creación (simulada)
if respuesta_creacion["Message"] == "Función Lambda creada exitosamente.":
  print(f"Función Lambda creada exitosamente: {respuesta_creacion['FunctionArn']}")
else:
  print("Error al crear la función Lambda.")

# Simulando la obtención de información de la función Lambda
print(f"Simulando obtención de información de la función Lambda: {nombre_funcion}")
informacion_funcion = {
  "FunctionName": nombre_funcion,
  "Runtime": "python3.8",
  "Handler": "handler_lambda",
  "Role": nombre_rol_iam
}

# Mostrando la información de la función Lambda (simulada)
print(f"Información de la función: {informacion_funcion}")
