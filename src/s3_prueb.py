import json
import boto3

# Configurar el cliente de S3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Nombre del bucket y nombre del archivo en S3
    bucket_name = 'mi-bucket'
    file_key = 'archivo.txt'

    try:
        # Obtener el contenido del archivo desde S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')

        # Procesar el contenido o realizar otras operaciones
        processed_content = content.upper()

        # Guardar el archivo procesado de vuelta en S3
        s3_client.put_object(Bucket=bucket_name, Key='archivo_procesado.txt', Body=processed_content.encode('utf-8'))

        # Devolver una respuesta exitosa
        return {
            'statusCode': 200,
            'body': json.dumps('Archivo procesado y guardado correctamente en S3.')
        }

    except Exception as e:
        # Manejar cualquier error y devolver una respuesta de error
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error al procesar y guardar el archivo en S3: {str(e)}')
        }