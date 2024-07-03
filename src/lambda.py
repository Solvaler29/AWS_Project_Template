import json
import boto3

# Configura el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = 'NombreDeTuTablaDynamoDB'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Ejemplo de función Lambda que guarda datos en DynamoDB
    try:
        # Procesa los datos recibidos
        data = json.loads(event['body'])
        item = {
            'id': data['id'],
            'nombre': data['nombre']
        }

        # Guarda los datos en DynamoDB
        table.put_item(Item=item)

        # Respuesta exitosa
        return {
            'statusCode': 200,
            'body': json.dumps('Datos guardados exitosamente en DynamoDB')
        }
    except Exception as e:
        # Manejo de errores
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error al procesar y guardar datos: {str(e)}')
        }