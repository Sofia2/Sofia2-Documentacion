.. figure::  ./images/logo_sofia2_grande.png
 :align:   center
 
Tecnologías de Referencia
=========================

* **Java** como Plataforma de desarrollo de módulos de proceso:

  * **Spring y su ecosistema** como tecnología de soporte.
  * **Despliegue estándar JEE** independiente de AppServer.
  
.. figure::  ./images/logo_java.png    

.. figure::  ./images/logo-spring.jpg
  
  
* **Datagrid (Hazelcast)** para comunicación entre módulos y HA.

* **Motor CEP (Siddhi CEP)** para reglas sobre grandes volúmenes de eventos en los que interviene el tiempo.

* **Motor Scripting (Groovy)** que permite definir reglas ante llegada de mensajes , soportando creación de nuevas operaciones (alarmas, notificaciones,…).

* **Hazelcast** como DataGrid soporte HA SIBs.

* **MongoDB** como RealTime DB por su almacenamiento JSON, escalabilidad,…

* **Hadoop** como Historical DB, los datos que ya no son del tiempo real se pasan automáticamente según configuración a este repositorio:

  * **Hive** como datawarehouse.
  * **Impala** como motor de consultas online distribuido.
  
* **MQTT/WebSockets/REST/WS/…** como protocolos de comunicación con la plataforma.

* **Spring MVC + Thymeleaf + jQuery** como framework Web para el desarrollo de la consola web

Con la modularidad de la solución se pueden llegar a sustituir o reemplazar algunas piezas si existe la necesidad. Por ejemplo BDH sobre Mongo, BDTR sobre Oracle,…
