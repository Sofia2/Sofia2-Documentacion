.. figure::  ./images/logo_sofia2_grande.png
 :align:   center
 
Tecnologías de Referencia
=========================

* **Java** como Plataforma de desarrollo de módulos de proceso:

  * **Spring y su ecosistema** como tecnología de soporte.
  * **Despliegue estándar JEE** independiente de AppServer.
                                           |logojava| |logospring| |logospringxd|
  

* **Motor CEP (Siddhi CEP)** para reglas sobre grandes volúmenes de eventos en los que interviene el tiempo.

* **Motor Scripting (Groovy, R y Phyton)** que permite definir reglas ante llegada de mensajes , soportando creación de nuevas operaciones (alarmas, notificaciones,…).

* **Hazelcast** como DataGrid para soporte y comunicación entre módulos y HA SIBs.  

                                           |logohazelcast|

* **MongoDB** como RealTime DB por su almacenamiento JSON, escalabilidad,…
                                           |logomongodb|
  

* **Hadoop** como Historical DB, los datos que ya no son del tiempo real se pasan automáticamente según configuración a este repositorio:

  * **Hive** como datawarehouse.
  * **Impala** como motor de consultas online distribuido.

.. figure::  ./images/logo-hadoop.jpg
.. figure::  ./images/logo-hive.jpg
.. figure:: ./images/logo-cloudera.png

* **MQTT/WebSockets/REST/WS/…** como protocolos de comunicación con la plataforma.

* **Spring MVC + Thymeleaf + jQuery** como framework Web para el desarrollo de la consola web

.. figure::  ./images/logo-javascripts.png

Con la modularidad de la solución se pueden llegar a sustituir o reemplazar algunas piezas si existe la necesidad. Por ejemplo BDH sobre Mongo, BDTR sobre Oracle,…

.. figure::  ./images/logo-apache.png



.. |logojava| image::  ./images/logo-java.png           
.. |logospring| image::  ./images/logo-spring.jpg
.. |logospringxd| image::  ./images/logo-springxd.png
.. |logohazelcast|  ./images/logo-hazelcast.png
.. |logomongodb|  ./images/logo-mongodb.png 


