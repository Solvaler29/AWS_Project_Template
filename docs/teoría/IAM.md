# Amazon IAM (Identity and Access Management)
La Gestión de Identidad y Acceso (IAM o IdAM para abreviar) es una forma de saber quién es un usuario y qué puede hacer. IAM es como el portero de un club nocturno con una lista de quién entra, quién no y quién entra al área VIP. IAM también se conoce como Gestión de Identidades (IdM).

## Definición general

En términos más técnicos, IAM es una forma de gestionar un conjunto de identidades digitales de usuarios y los privilegios asociados con cada identidad. Es un término amplio que cubre muchos productos diferentes que funcionan de la misma manera. En una organización, IAM puede ser un solo producto, un conjunto de procesos, productos de software, servicios en la nube y herramientas que brindan a los administradores visibilidad y control de los datos organizacionales involucrados para los usuarios individuales.
* Crear y asignar un IAM Role con políticas detalladas para la función Lambda.
* Configurar políticas de seguridad detalladas para la función Lambda.
* Crear un rol IAM con permisos básicos para Lambda.
* Asociar el rol IAM a la función Lambda.

## Control de Acceso Granular:

* **Políticas de Permisos Personalizadas:** Define políticas detalladas para otorgar permisos específicos a usuarios y roles según las necesidades de acceso.
* Grupos y Roles: Crea grupos y roles para gestionar permisos de forma centralizada, facilitando la administración de usuarios con necesidades similares.

## Seguridad Mejorada:

* **Autenticación Multifactor (MFA):** Añade una capa adicional de seguridad solicitando múltiples métodos de verificación antes de conceder el acceso.

## Gestión de Usuarios y Grupos:

* **Usuarios Federados:** Permite a los usuarios de tu organización acceder a AWS utilizando sus credenciales existentes mediante la federación de identidad.
 * Roles y Asignaciones Temporales: Usa roles para conceder permisos temporales a aplicaciones y servicios, reduciendo la necesidad de credenciales permanentes.
## Auditoría y Monitoreo:

* **Registros de Actividad (CloudTrail):** Realiza un seguimiento detallado de las acciones realizadas en tu cuenta de AWS para auditorías y cumplimiento normativo.
* **Alertas y Notificaciones:** Configura alertas para actividades sospechosas o inusuales, mejorando la capacidad de respuesta ante incidentes de seguridad.

## Facilidad de Integración:

* **SDKs y API:** Utiliza SDKs y API de AWS para automatizar y gestionar de manera programática los accesos y permisos en tus aplicaciones.

## Políticas Basadas en Recursos:

* **Permisos Directos en Recursos:** Define políticas directamente en recursos específicos como S3 buckets(un contenedor para objetos almacenados), asegurando un control preciso y adecuado de los accesos.
* **Control de Acceso Condicional:** Implementa condiciones específicas (como IP, tiempo, etc.) para restringir accesos a los recursos bajo determinadas circunstancias.