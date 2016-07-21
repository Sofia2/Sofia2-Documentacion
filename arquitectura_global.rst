.. figure::  ./images/logo_sofia2_grande.png
 :align:   center
 
Arquitectura global
===================

Esta Vista describe la Plataforma desde el punto de Vista de los módulos funcionales que componen la Plataforma:

.. figure::  ./images/VistaGeneralxModulos.png
 :align:   center


Módulos IoT
-----------
Éstos son los módulos necesarios para dar soporte a sistemas IoT:

* **SDKs**: La plataforma provee un set de herramientas para desarrolladores.

* **Sofia2 Control Panel**: La Plataforma ofrece una completa web de administración/configuración que permite gestionar todos los conceptos que maneja la Plataforma.

* **IoT Gateway**: Capa de abstracción del protocolo de comunicación, que implementa el protocolo SSAP (Smart Space Access Protocol), sobre diferentes protocolos (MQTT, MQTTS, Websockets, WS, REST).

* **Semantic Broker**: Módulo de la Plataforma que recibe, procesa y almacena toda la información de las aplicaciones, sensores y dispositivos conectados, actuando como Bus de Interoperabilidad.

* **Process**: Módulo que incluye 2 motores para la definición de reglas a aplicar sobre la información que entra en la Plataforma: el motor de Reglas (Sofia2-Rules) y el motor CEP (Sofia2-CEP).

* **Sofia2 Storage**: Modulo de almacenamiento de la información de la plataforma.

* **Sofia2 API Manager**: permite publicar la información gestionada por la plataforma como APIs REST y disponibilizar Servicios REST externos a la Plataforma.

* **Holystic Viewer**: módulo de visualización avanzada de la Plataforma, que soporta diferentes motores. 


Módulos Big Data
----------------


