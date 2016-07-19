.. figure::  ./images/logo_sofia2_grande.png
 :align:   center
 
Seguridad
=========

La Plataforma ofrece diferentes mecanismos de seguridad que permiten garantizar la privacidad de los datos, el control de acceso a los mismos y el envío de información cifrada a través de sus comunicaciones.

La capa de seguridad es aplicada en diferentes niveles: autenticación, autorización, y cifrado, asegurando las siguientes características:
* Comunicación segura y confidencial en cualquier tipo de conexión, ya sea entre clientes y plataforma o en cualquiera de los puntos de acceso disponibles (UI, APIs…), a través de SSL y/o HTTPS.

* Privacidad de los datos: asegurando el acceso exclusivo de aquellos usuarios que disponen de las credenciales necesarias para el acceso a la información correspondiente.

* Autenticación de los clientes de la Plataforma en la comunicación con esta a través de diversos mecanismos: usuario+ password, token, certificado.

* Autorización en el acceso a los datos, permitiendo controlar a grano fino (por ejemplo quien puede insertar qué información y quien puede consultar qué información).

* Capacidad de configurar y extender cada uno de los conceptos mencionados a través de los mecanismos de extensión de la plataforma. 

* Gestión de usuarios y roles: La plataforma consta de un sistema de roles gestionable desde la consola centralizada, permitiendo la asignación de roles a usuarios, asignación de permisos sobre información almacenada en la plataforma. Estos roles pueden almacenarse en diversos repositorios entre ellos LDAP.
