import boto3  # Importa la biblioteca boto3 para interactuar con AWS

class IAMRoleManager:
    def __init__(self, region_name):
        # Inicializa la clase IAMRoleManager con la región especificada
        self.region_name = region_name
        self.iam_client = boto3.client('iam', region_name=region_name)  # Crea un cliente IAM para la región especificada

    def crear_rol_lambda_basico(self, nombre_rol):
        # Método para crear un rol IAM básico para Lambda con el nombre proporcionado
        print(f"Creando rol IAM: {nombre_rol}")
        # Crea el rol IAM con la política de permisos para que Lambda pueda asumir este rol
        respuesta_rol = self.iam_client.create_role(
            RoleName=nombre_rol,
            AssumeRolePolicyDocument=json.dumps({
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "lambda.amazonaws.com"
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            })
        )

        # Adjunta la política básica de ejecución de Lambda al rol recién creado
        politicas_adjuntas = self.iam_client.attach_role_policy(
            RoleName=nombre_rol,
            PolicyArn="arn:aws:iam::aws:policy/AWSLambdaBasicExecutionRole"
        )

        print(f"Políticas adjuntas al rol: {politicas_adjuntas['AttachedPolicies']}")
        return respuesta_rol['Role']['Arn']  # Devuelve el ARN del rol creado

    def asociar_rol_a_funcion_lambda(self, nombre_rol_iam, nombre_funcion_lambda):
        # Método para asociar un rol IAM existente a una función Lambda
        print(f"Asociando rol IAM: {nombre_rol_iam} a la función Lambda: {nombre_funcion_lambda}")
        # Actualiza la configuración de la función Lambda para usar el rol IAM especificado
        self.iam_client.update_function_configuration(
            FunctionName=nombre_funcion_lambda,
            Role=nombre_rol_iam
        )
        print("Rol IAM asociado exitosamente.")

class LambdaManager:
    def __init__(self, region_name):
        # Inicializa la clase LambdaManager con la región especificada
        self.region_name = region_name
        self.lambda_client = boto3.client('lambda', region_name=region_name)  # Crea un cliente Lambda para la región especificada

    def crear_funcion_lambda(self, nombre_funcion, codigo_funcion, handler_funcion, nombre_rol_iam):
        # Método para crear una función Lambda con el nombre, código, handler y rol IAM especificados
        print(f"Creando función Lambda: {nombre_funcion} en la región: {self.region_name}")
        # Crea la función Lambda con el código proporcionado desde S3 y el rol IAM especificado
        respuesta_creacion = self.lambda_client.create_function(
            FunctionName=nombre_funcion,
            Runtime="python3.8",
            Handler=handler_funcion,
            Role=nombre_rol_iam,
            Code={
                "SourceCode": json.dumps({"S3Bucket": "no-es-necesario", "S3Key": codigo_funcion})
            }
        )

        # Verifica si la creación fue exitosa y devuelve el ARN de la función Lambda creada
        if 'FunctionArn' in respuesta_creacion:
            print(f"Función Lambda creada exitosamente: {respuesta_creacion['FunctionArn']}")
            return respuesta_creacion['FunctionArn']
        else:
            print("Error al crear la función Lambda.")
            return None


# Ejemplo de uso:

# Crea un objeto IAMRoleManager para la región 'us-east-1'
iam_role_manager = IAMRoleManager("us-east-1")

# Crea un rol IAM básico para Lambda con un nombre específico
nombre_rol_lambda_basico = "rol_lambda_basico"
arn_rol_lambda_basico = iam_role_manager.crear_rol_lambda_basico(nombre_rol_lambda_basico)

# Asocia el rol IAM creado a una función Lambda existente
nombre_funcion_lambda = "funcion_lambda_ejemplo"
iam_role_manager.asociar_rol_a_funcion_lambda(arn_rol_lambda_basico, nombre_funcion_lambda)
