Escalabilidad
=============

La robustez, escalabilidad y alta disponibilidad de la Plataforma se garantiza a diversos niveles:

* Volumen de almacenamiento.
* Procesado de datos.
* Velocidad de proceso de la información.
* Capacidad de respuesta en tiempo real.

La plataforma Sofia2 se construye sobre piezas que soportan y garantizan la robustez y escalabilidad horizontal.

Relacionado con esta escalabilidad horizontal está el hecho de que la plataforma esté concebida y pensada para correr sobre hardware commodity de modo que para aumentar la capacidad de procesamiento baste con incluir máquinas al clúster. 

|
Escalabilidad Ingest + Process (IoT Gateway + Semantic Broker)
--------------------------------------------------------------

* Ofrece escalabilidad horizontal en el procesado de datos, de modo que incorporando nuevas máquinas a la Plataforma esta incrementa su capacidad de procesamiento de forma lineal.
* Ofrece robustez al estar basado en la Plataforma Java.
* Ofrece alta disponibilidad ya que se crea un clúster de instancias de modo que el trabajo se redistribuye automáticamente.


|
Escalabilidad almacenamiento (Sofia2 Storage)
---------------------------------------------

El almacenamiento de la plataforma también cumple los criterios:

* Como BDH usa Hadoop:
  - vía su sistema de ficheros distribuido HDFS garantiza la alta disponibilidad.
  - Vía su Arquitectura YARN garantiza la escalabilidad horizontal.
* Como BDTR se usa MongoDB: 
  - A través de sharding permite escalado horizontal.
  - A través de su Arquitectura garantiza robustez y alta disponibilidad con Arquitectura Maestro-esclavo. 

|
Escalabilida Sofia2 PaaS
------------------------

Permite el auto escalado de las siguientes formas:

* Escalabilidad Vertical: Está asociada al incremento de las capacidades de cómputo y/o memoria de la una instancia concreta.
* Escalabilidad Horizontal: Está asociada a la variación de número de instancias para mantener el nivel de servicio en base a la demanda real del sistema.
* Escalabilidad Híbrida: Modelo en el que se puede optar por ambas opciones dependiendo de las necesidades del proyecto.

|
Sofia2-PaaS ofrece capacidades de elasticidad Horizontal transparente, es decir, analiza la demanda del servicio y realiza automáticamente los procesos necesarios de provisión y des-provisión de la infraestructura necesaria para cubrir dicha demanda.



