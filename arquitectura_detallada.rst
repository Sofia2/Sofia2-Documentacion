.. figure::  ./images/logo_sofia2_grande.png
 :align:   center
 
Arquitectura Detallada
======================

A continuación vamos a describir los módulos que componen la Plataforma sobre la vista modular con más detalle:


Módulos IoT:

SDKs
----


Sofia2 Control Panel
--------------------
La Plataforma ofrece una **completa web de administración/configuración** que permite gestionar todos los conceptos que maneja la Plataforma. El resto de módulos de la Plataforma se operan/configuran desde este módulo, que persiste su configuración en la BDC (Base Datos Configuración) del Sofia2-Repository


|
Semantic Broker (SIB)
---------------------


|
IoT Gateway
-----------
Capa de abstracción del protocolo de comunicación, que implementa el protocolo SSAP (Smart Space Access Protocol). 

Este módulo se especializa en el esquema de comunicación con dispositivos, sensores y sistemas TI en un contexto IoT, donde se debe facilitar el uso de protocolos de comunicación ligeros en un entorno tecnológico heterogéneo. El protocolo SSAP proporciona tanto la ligereza del mensaje como su homogeneización a nivel de aplicación. De esta manera, la información gestionada por las subsiguientes capas de la plataforma es completamente agnóstica del protocolo tecnológico usado para el envío del dato, dando lugar a su gestión desde un punto de vista semántico.

Para agilizar la integración con la plataforma (desde sensores, dispositivos o sistemas TI), este componente ofrece la interpretación de multitud de protocolos “out of the box”:

* REST y WebSockets: para clientes Javascript, smartphones,..
* MQTT para comunicaciones bidireccionales y dispositivos básicos.
* Web Services/JMS/AMQP para aplicaciones empresariales.

Además, se facilita la incorporación de nuevos protocolos gracias al despliegue de nuevos Plugins.

Esto, sumado a las APIS multilenguaje `(Descargar) <http://sofia2.com/desarrollador.html#descargas>`_ que ofrece la plataforma facilita el desarrollo de cualquier cliente que quiera comunicarse con la plataforma, permitiendo la abstracción de los detalles técnicos del protocolo a utilizar (ya considerados en el API).


|
Process
-------
Se compone de los dos módulos siguientes:

 |
 Motor de Reglas (Sofia2-Rules)
 ------------------------------
 
 |
 Motor CEP (Sofia2-CEP)
 ----------------------

|
Sofia2 Storage
--------------

|
API Manager
-----------

|
Holystic Viewer
---------------
 
| 
| 
Módulos Big Data:

|
Sofia2 DataFlow
---------------

|
Sofia2 Notebooks
----------------

|
Sofia2 ML
---------

|
Sofia2 DataLink
---------------



