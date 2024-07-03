import boto3
import subprocess

def deploy_stack(stack_name, template_file):
    try:
        # Configura el cliente de CloudFormation
        cloudformation = boto3.client('cloudformation')

        # Despliega la pila utilizando el archivo template.yaml
        print(f"Desplegando la pila {stack_name}...")
        response = cloudformation.create_stack(
            StackName=stack_name,
            TemplateBody=open(template_file, 'r').read(),
            Capabilities=['CAPABILITY_IAM']
        )

        # Espera hasta que la operación de despliegue se complete
        print("Esperando a que la pila se despliegue...")
        cloudformation.get_waiter('stack_create_complete').wait(StackName=stack_name)
        print("Despliegue completado exitosamente.")

    except Exception as e:
        print(f"Error durante el despliegue de la pila: {str(e)}")

if __name__ == '__main__':
    stack_name = 'NombreDeTuStack'
    template_file = 'template.yaml'

    # Llama a la función para desplegar la pila
    deploy_stack(stack_name, template_file)