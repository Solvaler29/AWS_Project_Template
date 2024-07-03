import boto3

class IAMRoleManager:
  def __init__(self, region_name):
    self.region_name = region_name
    self.iam_client = boto3.client('iam', region_name=region_name)

  def crear_rol_lambda_basico(self, nombre_rol):
    # Crear el rol IAM
    print(f"Creando rol IAM: {nombre_rol}")
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

    # Adjuntar políticas de IAM al rol
    politicas_adjuntas = self.iam_client.attach_role_policy(
      RoleName=nombre_rol,
      PolicyArn="arn:aws:iam::aws:policy/AWSLambdaBasicExecutionRole"
    )

    print(f"Políticas adjuntas al rol: {politicas_adjuntas['AttachedPolicies']}")
    return respuesta_rol['Role']['Arn']

  def asociar_rol_a_funcion_lambda(self, nombre_rol_iam, nombre_funcion_lambda):
    # Asociar el rol IAM a la función Lambda
    print(f"Asociando rol IAM: {nombre_rol_iam} a la función Lambda: {nombre_funcion_lambda}")
    self.iam_client.update_function_configuration(
      FunctionName=nombre_funcion_lambda,
      Role=nombre_rol_iam
    )
    print("Rol IAM asociado exitosamente.")

class SAMDeployer:
  def __init__(self, region_name, nombre_template, nombre_funcion_lambda, codigo_funcion_lambda, handler_funcion_lambda, nombre_rol_iam, evento_api_path, evento_api_metodo):
    self.region_name = region_name
    self.nombre_template = nombre_template
    self.nombre_funcion_lambda = nombre_funcion_lambda
    self.codigo_funcion_lambda = codigo_funcion_lambda
    self.handler_funcion_lambda = handler_funcion_lambda
    self.nombre_rol_iam = nombre_rol_iam
    self.evento_api_path = evento_api_path
    self.evento_api_metodo = evento_api_metodo

  def crear_template_yaml(self):
    # Crear el contenido del archivo template.yaml
    contenido_template = {
      "AWSTemplateFormatVersion": "2010-09-09",
      "Transform": "AWS::Serverless-2016-10-31",
      "Resources": {
        self.nombre_funcion_lambda: {
          "Type": "AWS::Serverless::Function",
          "Properties": {
            "Handler": self.handler_funcion_lambda,
            "Runtime": "python3.8",
            "CodeUri": "./",
            "Role": self.nombre_rol_iam,
            "Events": {
              "EventoAPI": {
                "Type": "Api",
                "Properties": {
                  "Path": self.evento_api_path,
                  "Method": self.evento_api_metodo
                }
              }
            }
          }
        }
      }
    }

    # Simular la creación del archivo template.yaml
    print(f"Simulando creación de archivo template.yaml: {self.nombre_template}")
    print(json.dumps(contenido_template, indent=4))

  def empaquetar_aplicacion(self):
    # Simular el empaquetado de la aplicación con SAM CLI
    print(f"Simulando empaquetado de la aplicación con SAM CLI")
    print("**Nota:** Se asume que el empaquetado se realiza correctamente.")

  def desplegar_aplicacion(self): # Fix: Indent this method definition to be part of the class
    # Simular el despliegue de la aplicación con SAM CLI
    print(f"Simulando despliegue de la aplicación con SAM CLI")


## Datos
region_name = "us-east-1"
nombre_template = "template.yaml"
nombre_funcion_lambda = "funcion_lambda_ejemplo"
codigo_funcion_lambda = "def handler_lambda(event, context): ... # Código de la función"
handler_funcion_lambda = "handler_lambda"
nombre_rol_iam = "rol_lambda_basico"
evento_api_path = "/"
evento_api_metodo = "GET"

# Crear objetos de las clases
iam_role_manager = IAMRoleManager(region_name)
sam_deployer = SAMDeployer(region_name, nombre_template, nombre_funcion_lambda, codigo_funcion_lambda, handler_funcion_lambda, nombre_rol_iam, evento_api_path, evento_api_metodo)

# Simular el despliegue
print("**Simulación del despliegue de una función Lambda con SAM usando clases en Python**")

# Crear el template.yaml
sam_deployer.crear_template_yaml()

# Empaquetar la aplicación
sam_deployer.empaquetar_aplicacion()

# Desplegar la aplicación
sam_deployer.desplegar_aplicacion()

print("\n**Simulación finalizada**")
