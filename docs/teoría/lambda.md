# AWS Lambda
AWS Lambda es un servicio de computación serverless que te permite ejecutar código sin aprovisionar ni administrar servidores. A continuación, se detallan diferentes aspectos relacionados con su uso, características, funciones, despliegue y administración, monitoreo y registro, así como mejores prácticas para el desarrollo.

## Usos: 
AWS Lambda se utiliza principalmente para ejecutar código en respuesta a eventos. Esto incluye: 

* **Eventos de API Gateway:** Procesamiento de solicitudes HTTP.
* **Eventos de S3:** Procesamiento de archivos cargados.
* **Eventos de DynamoDB:** Procesamiento de cambios en la base de datos.
* **Eventos de CloudWatch:** Programación de ejecuciones periódicas.

## Características 

* **Serverless:**
AWS Lambda es un servicio serverless, lo que significa que elimina la necesidad de gestionar la infraestructura subyacente. No es necesario aprovisionar ni administrar servidores. En su lugar, AWS se encarga de la infraestructura, como el aprovisionamiento de recursos y la gestión del sistema operativo.

* **Elasticidad:**
Lambda escala automáticamente en respuesta a la carga de trabajo o a los eventos que desencadenan las funciones.

* **Integraciones:**
Integra fácilmente con otros servicios de AWS y servicios externos a través de API Gateway. Esto permite construir aplicaciones serverless(modelo de computación en la nube) complejas que responden a eventos desde servicios como Amazon S3, DynamoDB, SNS, y más. 

* **Pay-as-you-go:**
Con Lambda, solo pagas por el tiempo de cómputo que consumes y la cantidad de recursos utilizados. Permite optimizar los costos al alinear los gastos con la cantidad exacta de recursos computacionales utilizados por tus funciones Lambda.

## Funciones


* **Desarrollo de Funciones:** Escribir funciones en lenguajes como Python, Node.js, Java, etc.

* **Integración con Otros Servicios:** Conexión directa con servicios como S3, DynamoDB, SNS, etc.

* **Personalización de Entorno:** Configuración de variables de entorno y ajustes de memoria y tiempo de ejecución.

## Monitoreo y Registro
* **CloudWatch logs:** Registro de eventos y salida de las funciones Lambda.

* **Métricas Personalizadas:** Configuración de métricas para monitorizar el rendimiento y la salud.

* **Integración con X-Ray:** Rastreo de solicitudes para diagnóstico de problemas de rendimiento.