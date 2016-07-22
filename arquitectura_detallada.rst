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
La Plataforma ofrece una **completa web de administración/configuración** que permite gestionar todos los conceptos que maneja la Plataforma. 

El resto de módulos de la Plataforma se operan/configuran desde este módulo, que persiste su configuración en la BDC (Base Datos Configuración) del Sofia2-Repository.


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
 El módulo Sofia2-Rules permite ampliar el funcionamiento de la Plataforma permitiendo definir reglas que se ejecutan ante ciertas condiciones (inserción de un nuevo dato o cada cierto tiempo). 
 
Estas reglas dan la capacidad de definir, en base a Scripting, acciones que ejecuta la Plataforma. Gracias a ellas se pueden gestionar y tratar los datos de la plataforma. 

Por ejemplo se pueden definir transformaciones a los datos existentes o implementar el motor de reglas en tiempo real sobre patrones/datos/eventos. 

Todas estas reglas se crean desde la Consola Web de forma sencilla y sin programar. La creación de reglas desde la consola va en función del rol, por ejemplo usuario administrador puede crear reglas sobre cualquier ontología mientras que un usuario colaborador puede definir reglas sobre ontologías de las que es propietario.

La Plataforma disponibiliza  un conjunto de acciones predefinidas que se pueden ejecutar dentro de la regla, como Enviar Mail, Generar Alarma,… Además, se pueden crear nuevas acciones predefinidas en tiempo de desarrollo.


Podemos diferenciar dos tipos de Reglas Scripting:

* **Reglas Temporizadas**. Ejecutan el Script definido cada X segundos definidos en la creación de la regla, este tipo de Reglas únicamente define el THEN pues no existe un flujo alternativo a una condición.

* **Reglas Ontología**. Son reglas asociadas a una Ontología y por lo tanto únicamente entran en acción cuando se realiza la inserción de una Instancia de Ontología en el SIB. Definen una condición sobre un valor de la instancia de la Ontología, con los operadores  (=,>,<, ¡=), está escrito en lenguaje Groovy e interpretado como un Script.

Las reglas pueden ser desarrolladas en Groovy (lenguaje sencillo y de alta productividad basado en Java), Python, R o directamente en Java.

Los scripts pueden ser desplegados en caliente en la Plataforma, de forma que pueden actuar en tiempo real directamente tras su creación.
 
La ejecución de cada uno de los Script se realiza de forma independiente de la JVM que gestiona el SIB aislando al SIB y los diferentes Script de posibles errores. 


Las Reglas se desarrollan haciendo uso de una biblioteca de APIS que permiten interactuar con los diferentes elementos de la plataforma (p.e. ontologías, BDTR) y con elementos externos a ella (p.e. envío de correos, redes sociales). Estas APIS son extensibles por el administrador de forma sencilla, estando disponibles out-of-the-box librerías para gestión de conexiones HTTP, JMS, LOGS, mail, BDTR, ejecución de Scripts, SSAP, Twitter, entre otras.


 
 |
 Motor CEP (Sofia2-CEP)
 ----------------------

|
Sofia2 Storage
--------------
Con el objetivo de garantizar que, para cada momento del ciclo de vida de la información, ésta se gestiona de la menor manera, la plataforma plantea el uso de tres repositorios distintos que se complementan y comunican componiendo una solución de almacenamiento completa:

.. figure::  ./images/Sofia2Storage.JPG
 :align:   center
 


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
Permite hacer ingesta masiva de datos desde multitud de fuentes, transformaciones simples online sobre la información y ruteado hacia otro destino (módulo IoT Flow, BDTR, BDH,…). Es posible añadir plugins a la plataforma para incorporar nuevas fuentes, transformaciones y destinos.

La composición del proceso ETL (Extracción, Transformación y Carga o Load), se realiza mediante el drag&drop  de las tareas disponibles en la barra de herramientas.

.. figure::  ./images/dataflow1.png
 :align:   center


En tiempo de ejecución, Se pueden configurar reglas para capturar y visualizar datos de un pipeline en ejecución. Además es posible consultar las estadísticas de ejecución de cualquier pipeline en tiempo real, los datos procesados y el historial del pipeline,

.. figure::  ./images/dataflow2.png
 :align:   center

La configuración de alertas y thresholds de normalidad posibilitan la ejecución de acciones automáticas como la comunicación de estos eventos y la visualización del detalle.


|
Sofia2 Notebooks
----------------

|
Sofia2 ML
---------

|
Sofia2 DataLink
---------------



