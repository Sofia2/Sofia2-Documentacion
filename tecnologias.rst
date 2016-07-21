.. figure::  ./images/logo_sofia2_grande.png
 :align:   center
 
Tecnologías de Referencia
=========================

* |logojava|  como Plataforma de desarrollo de módulos de proceso:

  * |logospring| **y su ecosistema** como tecnología de soporte.
  
  * |logospringxd| para la ingesta de datos, analítica en tiempo real, procesamiento batch y exportación de datos.
  
  * **Despliegue estándar JEE** independiente de AppServer.



* **Motor CEP (Siddhi CEP)** para reglas sobre grandes volúmenes de eventos en los que interviene el tiempo.


* **Motor Scripting (Groovy, R y Phyton)** que permite definir reglas ante llegada de mensajes , soportando creación de nuevas operaciones (alarmas, notificaciones,…).

                                             |logogroovy| |logor| |logophyton|


* |logohazelcast| como DataGrid para soporte y comunicación entre módulos y HA SIBs.  


* |logomongodb| como RealTime DB por su almacenamiento JSON, escalabilidad,…


* |logohadoop| como Historical DB, los datos que ya no son del tiempo real se pasan automáticamente según configuración a este repositorio:

  * |logohive| como datawarehouse.
  * |logoimpala| como motor de consultas online distribuido.



* **MQTT/WebSockets/REST/WS/…** como protocolos de comunicación con la plataforma.

* **Spring MVC + Thymeleaf + jQuery** como framework Web para el desarrollo de la consola web

.. figure::  ./images/logo-javascripts.png

Con la modularidad de la solución se pueden llegar a sustituir o reemplazar algunas piezas si existe la necesidad. Por ejemplo BDH sobre Mongo, BDTR sobre Oracle,…

.. figure::  ./images/logo-apache.png
.. figure::  ./images/logo-apachedrill.png
.. figure::  ./images/logo-scala.jpg
.. figure::  ./images/logo-zeppelin.png


.. |logojava| image::  ./images/logo-java.png           
.. |logospring| image::  ./images/logo-spring.jpg
.. |logospringxd| image::  ./images/logo-springxd.png
.. |logohazelcast| image:: ./images/logo-hazelcast.png
.. |logomongodb| image:: ./images/logo-mongodb.png
.. |logohadoop| image::  ./images/logo-hadoop.jpg
.. |logohive| image::  ./images/logo-hive.jpg
.. |logoimpala| image:: ./images/logo-cloudera.png
.. |logogroovy| image:: ./images/logo-groovy.png
.. |logor| image:: ./images/logo-r.png
.. |logophyton| image:: ./images/logo-python.jpg


