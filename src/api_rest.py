import json

# Datos de ejemplo
data = {
    "items": [
        {"id": 1, "name": "Item 1", "price": 10.99},
        {"id": 2, "name": "Item 2", "price": 15.99},
        {"id": 3, "name": "Item 3", "price": 20.99},
    ]
}

def lambda_handler(event, context):
    # Determinar el método HTTP de la solicitud
    http_method = event["httpMethod"]

    # Manejar solicitud GET
    if http_method == "GET":
        # Devolver los datos en la respuesta
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # Manejar solicitud POST
    elif http_method == "POST":
        # Obtener el cuerpo de la solicitud y analizarlo como JSON
        body = json.loads(event["body"])
        # Agregar los datos recibidos a los datos de ejemplo
        data["items"].append(body)
        # Devolver los datos actualizados en la respuesta
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # Manejar solicitud PUT
    elif http_method == "PUT":
        # Obtener el cuerpo de la solicitud y analizarlo como JSON
        body = json.loads(event["body"])
        # Actualizar los datos de ejemplo con los datos recibidos
        for item in data["items"]:
            if item["id"] == body["id"]:
                item.update(body)
                break
        # Devolver los datos actualizados en la respuesta
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # Manejar solicitud DELETE
    elif http_method == "DELETE":
        # Obtener el cuerpo de la solicitud y analizarlo como JSON
        body = json.loads(event["body"])
        # Encontrar el ítem con el id especificado en los datos de ejemplo
        for i, item in enumerate(data["items"]):
            if item["id"] == body["id"]:
                # Eliminar el ítem de los datos de ejemplo
                del data["items"][i]
                break
        # Devolver los datos actualizados en la respuesta
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    else:
        # Devolver un mensaje de error para métodos no soportados
        response = {
            "statusCode": 405,
            "body": json.dumps({"error": "Método no permitido"})
        }
        return response
