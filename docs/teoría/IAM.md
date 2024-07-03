# Amazon IAM (Identity and Access Management)
Servicio web de AWS que ayuda a controlar de manera segura el acceso a los recursos de AWS. Permite gestionar usuarios, grupos y permisos, garantizando que cada recurso en AWS tenga los accesos adecuados.

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