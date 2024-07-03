import json
import boto3

class DynamoDBManager:
  def __init__(self, region_name, nombre_tabla, nombre_rol_iam):
    self.region_name = region_name
    self.nombre_tabla = nombre_tabla
    self.nombre_rol_iam = nombre_rol_iam

    # Cliente de DynamoDB
    self.dynamodb = boto3.client('dynamodb', region_name=self.region_name)

  def guardar_datos(self, datos):
    # Preparar los datos para DynamoDB
    item_dynamodb = {
      "id": datos["id"],
      "nombre": datos["nombre"],
      "correo": datos["correo"]
    }

    # Guardar los datos en DynamoDB
    try:
      self.dynamodb.put_item(TableName=self.nombre_tabla, Item=item_dynamodb)
      print(f"Datos guardados exitosamente: {item_dynamodb}")
      return True
    except Exception as e:
      print(f"Error al guardar datos: {e}")
      return False

  def obtener_datos_por_id(self, id_buscado):
    # Buscar el elemento por ID en DynamoDB
    try:
      respuesta_dynamodb = self.dynamodb.get_item(TableName=self.nombre_tabla, Key={'id': {'S': id_buscado}})
      if 'Item' in respuesta_dynamodb:
        item_encontrado = respuesta_dynamodb['Item']
        datos = {
          "id": item_encontrado['id']['S'],
          "nombre": item_encontrado['nombre']['S'],
          "correo": item_encontrado['correo']['S']
        }
        print(f"Datos encontrados para ID: {id_buscado}: {datos}")
        return datos
      else:
        print(f"No se encontraron datos para el ID: {id_buscado}")
        return None
    except Exception as e:
      print(f"Error al obtener datos por ID: {e}")
      return None

  def actualizar_datos(self, datos):
    # Preparar los datos para la actualización
    item_actualizado = {
      "id": datos["id"],
      "nombre": datos["nombre"],
      "correo": datos["correo"]
    }

    # Actualizar los datos en DynamoDB
    try:
      self.dynamodb.update_item(TableName=self.nombre_tabla, Key={'id': {'S': datos["id"]}}, UpdateExpression="SET nombre = :nombre, correo = :correo", ExpressionAttributeValues={':nombre': {'S': datos["nombre"]}, ':correo': {'S': datos["correo"]}})
      print(f"Datos actualizados exitosamente: {item_actualizado}")
      return True
    except Exception as e:
      print(f"Error al actualizar datos: {e}")
      return False

  def eliminar_datos_por_id(self, id_eliminar):
    # Eliminar el elemento por ID en DynamoDB
    try:
      self.dynamodb.delete_item(TableName=self.nombre_tabla, Key={'id': {'S': id_eliminar}})
      print(f"Datos eliminados exitosamente para ID: {id_eliminar}")
      return True
    except Exception as e:
      print(f"Error al eliminar datos por ID: {e}")
      return False

dynamodb_manager = DynamoDBManager("us-east-1", "MiTabla", "rol_dynamodb_lambda")

# Guardar datos
datos_nuevos = {
  "id": "123",
  "nombre": "Juan Pérez",
  "correo": "juan.perez@ejemplo.com"
}

if dynamodb_manager.guardar_datos(datos_nuevos):
  print("Datos guardados correctamente.")
else:
  print("Error al guardar datos.")

# Obtener datos por ID
id_buscado = "123"
datos_obtenidos = dynamodb_manager.obtener_datos_por_id(id_buscado)

if datos_obtenidos:
 print(f"Datos obtenidos para ID: {id_buscado}: {datos_obtenidos}")
else:
  pass