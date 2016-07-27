+----------------------------------------------------+----+----+
| |image0|                                           |
|                                                    |
| TCO de sofia2                                      |
|                                                    |
| vs desarrollo a medida sobre una base relacional   |
|                                                    |
| Abril 2015                                         |
|                                                    |
| Versión 1                                          |
+----------------------------------------------------+----+----+
|                                                    |
+----------------------------------------------------+----+----+
| |image1|                                           |    |    |
+----------------------------------------------------+----+----+

INDICE
======

`**1** **INDICE** 2 <#indice>`__

`**2** **Introducción** 3 <#introducción>`__

`**2.1** **Objetivos y alcance del presente documento** 3 <#objetivos-y-alcance-del-presente-documento>`__

`**3** **Qué es Sofia2** 4 <#qué-es-sofia2>`__

`**4** **Coste Total de Propiedad (TCO)** 5 <#_Toc417046153>`__

`**4.1** **Costes Iniciales** 5 <#_Toc417046154>`__

`**4.2** **Costes Corrientes** 5 <#_Toc417046155>`__

`**5** **Comparación del coste total de propiedad** 6 <#_Toc417046156>`__

`**5.1** **Esfuerzo de desarrollo inicial** 6 <#_Toc417046157>`__

`**5.2** **Esfuerzo administrativo inicial** 7 <#esfuerzo-administrativo-inicial>`__

`**5.3** **Licencias de software** 8 <#licencias-de-software>`__

`**5.4** **Hardware de servidores** 8 <#hardware-de-servidores>`__

`**5.5** **Hardware de almacenamiento** 9 <#hardware-de-almacenamiento>`__

`**5.6** **Esfuerzo de desarrollo corriente** 9 <#esfuerzo-de-desarrollo-corriente>`__

`**5.7** **Esfuerzo administrativo corriente** 9 <#esfuerzo-administrativo-corriente>`__

`**5.8** **Mantenimiento y soporte técnico** 9 <#mantenimiento-y-soporte-técnico>`__

`**5.9** **Otras ventajas de Sofia2** 10 <#otras-ventajas-de-sofia2>`__

Introducción
============

Objetivos y alcance del presente documento
------------------------------------------

El presente documento describe el razonamiento empresarial para implementar Sofia2 en vez de un desarrollo tradicional con una base de datos relacional. Este informe hace una comparación entre el Coste Total de Propiedad de la Plataforma Sofia2 y el de un desarrollo a medida con una base de datos relacional, considerando los costes iniciales y corrientes (software, hardware y personal).

Qué es Sofia2
=============

Sofia2 surge de un proyecto I+D europeo denominado SOFIA.

SOFIA es el acrónimo de **SMART OBJECTS FOR INTELLIGENT APPLICATIONS** y es una plataforma que surge como de un proyecto de I +D Artemis de tres años finalizado en Marzo de 2012, en el que participan 19 partners de cuatro países de la UE, entre los cuales están Nokia, Philips, Fiat, Acciona e Indra.

Sofia2 es una Arquitectura middleware semántica que permite la interoperabilidad de múltiples sistemas y dispositivos. Permite poner información real a disposición de aplicaciones inteligentes, dando respuesta al emergente concepto del IoT (**Internet of Things**).

Entre otras cosas, Sofia2 es:

-  Open-source

-  Multiplataforma: disponible para Windows, Android, Linux, iOS,…

-  Multilenguaje: con APIs Java, Javascript, C++, Arduino

-  Agnóstica de las comunicaciones: con implementaciones TCP, MQTT, HTTP (REST, Websockets y WebServices), Ajax Push, etc.

-  Escalable horizontalmente: Su diseño permite mantener un rendimiento óptimo con solo añadir más máquinas al cluster, en caso de necesitar más potencia si aumenta la carga de trabajo.

-  Basada en estándares: Desde su implementación interna utilizando estándares del mercado (Java, Spring, MongoDB, etc.) hasta la publicación de servicios al exterior también mediante interfaces y métodos de comunicación estándar (HTTP, Rest, Web Services, etc.).

-  Agnóstica de las comunicaciones: con implementaciones TCP, MQTT, HTTP (REST y WebServices), Ajax Push,…

Coste Total de Propiedad (TCO)
==============================

Costes Iniciales
----------------

Los costes iniciales se componen de:

-  **Esfuerzo de desarrollo inicial**: Coste de personal + Programación del desarrollador necesaria para la aplicación

-  **Esfuerzo administrativo inicial**: Coste de personal + Administradores para instalar y configurar software, máquinas del clúster, particionado, …

-  **Licencias de software **

-  **Hardware de servidores**. Servidores necesarios para ejecutar la base de datos (se excluye almacenamiento). Depende principalmente del número y tipo de procesadores y RAM. Otros costes incluyen recintos, conexiones de red, cableado y suministros de alimentación

-  **Hardware de almacenamiento**. Almacenamiento necesario para almacenar los datos, varía en función de si se utiliza almacenamiento interno o compartido (SAN), de la cantidad de almacenamiento y de si se utilizan unidades de disco duro (HDD) o unidades de estado sólido (SSD).

Costes Corrientes 
------------------

Los costes corrientes se componen de:

-  **Esfuerzo de desarrollo corriente**: Personal + Programación necesaria para adaptar el almacén de datos a las necesidades del cliente, del mercado y empresariales

-  **Esfuerzo administrativo corriente**: Personal + Esfuerzo administrativo necesario para mantener el funcionamiento y ejecución del almacén de datos

-  **Mantenimiento y soporte técnico del software**: Mantenimiento: actualizaciones y soluciones de errores del software + Soporte técnico: asistencia para localizar y solucionar problemas técnicos en el software

-  **Mantenimiento y soporte técnico del hardware**: Mantenimiento: actualizaciones y soluciones de errores del firmware y cualquier software que pueda incluir el hardware + Soporte técnico: asistencia telefónica para localizar y solucionar problemas técnicos en el hardware

-  **Costes de despliegue diversos**: Otros costes necesarios para mantener la base de datos en funcionamiento. Incluye costes de nube/alojamiento/coubicación, costes de ancho de banda, tarifas eléctricas, etc.

Comparación del coste total de propiedad
========================================

A continuación veremos como Sofia2 reduce los diversos costes que componen el TCO de un sistema.

Esfuerzo de desarrollo inicial
------------------------------

El esfuerzo de desarrollo inicial se refiere al coste del tiempo dedicado por el desarrollador para conseguir que la aplicación y el almacén de datos trabajen juntos.

En el caso de un desarrollo sobre base de datos relacional, el esfuerzo de desarrollo inicial incluye tareas como definir el modelo de datos, crear una capa de mapeo objeto-relacional (ORM), escribir la lógica empresarial para la aplicación y hacer la capa de presentación para esta lógica.

Sofia2 está diseñado para que reducir los tiempos de desarrollo, de modo que un desarrollador en cualquier lenguaje pueda utilizar la Plataforma con facilidad.

Para eso a través de la Consola Sofia2 (Sofia2-Console) el desarrollador puede:

-  Crear sus entidades (Ontologías en Sofia2, tablas en un SGBDR, colecciones en MongoDB)

-  Definir sus reglas de negocio de forma sencilla y asistida

-  Establecer seguridad en el acceso a sus entidades

-  Acceso CRUD (consulta, inserción, borrado, actualización,…) a todas estas entidades a través de cualquier lenguaje (Java, Javascript, C, Android,…) lo que le permite desarrollar tanto aplicaciones Web MVC (API Java, Python, Node.js), aplicaciones HTML5 (API Javascript), aplicaciones móviles (API Android, iOS, Javascript…) o módulos de negocio (Java, Python, C,…)

-  Capacidad de suscripción a eventos, consultas, reglas, …de forma sencilla e independiente del protocolo de mensajería (JMS, MQTT, AMQP,…)

-  Publicación asistida y web de APIS REST a partir de las entidades

-  Capacidades GIS integradas

-  Dashboards integrados

-  Informes integrados

-  Repositorio Big Data integrado

Por lo tanto, podemos decir que resulta mucho más rentable desarrollar con Sofia2 que hacer un desarrollo a medida sobre bases de datos relacionales.

Otra ventaja de productividad importante de Sofia2 es su diseño de Entidades (Ontologías) orientado a documentos y a los esquemas dinámicos. La forma en que almacena datos de la aplicación se corresponde con la tecnología y prácticas de desarrollo actuales, que han evolucionado considerablemente desde los comienzos de la industria de las bases de datos relacionales hace 30 años.

Algunos motivos que respaldan las ventajas de productividad de Sofia2 son:

-  **Facilidad de uso**: Sofia2 es compatible con las metodologías de desarrollo actuales, permite a los desarrolladores realizar iteraciones de forma rápida y continua sobre el modelo de datos y todo desde un interfaz Web. En contraposición un desarrollo tradicional modelo relacional impone un estricto conjunto de limitaciones al desarrollo, tanto a nivel de modelo de datos, de creación de reglas, cambios,…

-  **Modelo de datos.** Con Sofia2, el desarrollador solo tiene que crear el modelo de datos en un lugar: la Consola Web del propio producto. En un desarrollo los desarrolladores necesitan crear y mantener el modelo de datos en tres lugares mediante el uso de diferentes interfaces: la aplicación, la propia base de datos y la capa ORM.

-  **Flexibilidad de datos**. A diferencia de una SGBDR, Sofia2 permite a los desarrolladores almacenar con facilidad datos polimórficos, así como datos semiestructurados y estructurados, en un almacén de datos individual.

-  **Soporte JSON**. El almacenamiento en JSON, pilar básico de numerosas aplicaciones actuales, se realiza sin dificultades y no requiere conversión. Con una SGBDR, los desarrolladores necesitan “aplanar” y transformar JSON para almacenarlo en tablas relacionales, y más tarde tienen que recuperar las capas al realizar la extracción de la base de datos.

Esfuerzo administrativo inicial
-------------------------------

La instalación y configuración de Sofia2 es económica y sencilla.

La Plataforma se compone de :

-  **BDC** **(Base Datos Configuración)** : puede ser cualquier base de datos relacional. Por defecto funciona sobre una BD embebida MySQL.

-  **BDTR** **(Base Datos Tiempo Real)**: en la RI es un MongoDB lo que hace que el esfuerzo administrativo inicial sea bajo, un administrador solo debe tener en cuenta una variable: el número de nodos en el clúster. Solo existe un reducido conjunto de ajustes de configuración para poner el sistema en funcionamiento. Los administradores de MongoDB no necesitan integrar capas de memoria caché ni crear lógica de particionado horizontal personalizada para dirigir las consultas al nodo servidor correcto. En lugar de esto, el almacenamiento en memoria, caché y el particionado horizontal son capacidades centrales de MongoDB.

-  **BDH** (**Base Datos Histórica)**: puede funcionar sobre MongoDB o Hadoop en función de las necesidades o preferencias.

-  **SIB + Consola + Tools + API Manager + Process**: todos los módulos de negocio de la Plataforma están construidos en Java, se despliegan como aplicaciones Web en cualquier servidor de aplicaciones JEE. El grueso de la configuración va en la BDC por lo que no es necesario crear ficheros de configuración complejos.

Licencias de software
---------------------

Sofia2 es una Plataforma con una versión gratuita para la comunidad de código abierto (licencia Apache) y una edición para suscriptores comerciales que puede usarse en modo On Premise o en Modo Cloud.

Esta versión incluye soporte técnico en diferentes modalidades (desde 8x5 sin SLAS a 24x7 con SLAS estrictas), actualizaciones de software y soluciones de errores y algunas funciones adicionales.

La edición comercial de Sofia2 se factura de forma continua en lugar de puntualmente (esto es, una cuota anual por servidor).

Hardware de servidores
----------------------

En general, los costes de servidores de Sofia2 son considerablemente inferiores a los de un desarrollo tradicional sobre BD relacional para cargas de trabajo y disponibilidad similar. Esto aplica a todos los componentes.

Sofia2 se diseña para utilizar hardware básico en arquitecturas escalables.

Los despliegues de Sofia2 normalmente utilizan servidores Linux básicos y económicos, que tienen un coste de tan solo 3.000 $; incluso un sistema de baja energía y alto rendimiento puede costar tan solo 4.000 $ (excluyendo almacenamiento).

Hardware de almacenamiento
--------------------------

La arquitectura escalable de Sofia2 permite reducir considerablemente los costes de almacenamiento.

Sofia2 puede utilizar el almacenamiento local económico y permite realizar un uso eficiente de las unidades de estado sólido (SSD).

Esfuerzo de desarrollo corriente
--------------------------------

Las dinámicas del esfuerzo de desarrollo corriente son menores a las del esfuerzo de desarrollo inicial.

Con una desarrollo tradicional, el coste de realizar cambios en la aplicación es mayor, bien sean cambios en el esquema de una base de datos que ya se encuentre en producción (coste mayor que para una base de datos que aún no se ha entregado), como en el desarrollo de la lógica, reglas, seguridad, configuración).

Por ejemplo con Sofia2 resulta fácil para los desarrolladores agregar campos a las entidades, crear nuevas APIs, lo que se deriva en costes considerablemente inferiores y permite a los desarrolladores adaptar las aplicaciones a medida que evolucionen las demandas.

Esfuerzo administrativo corriente
---------------------------------

El esfuerzo administrativo corriente incluye actividades que mantienen el sistema en buen estado de funcionamiento (por ejemplo, actualización del software y hardware, realización de copias de seguridad y recuperación de tiempos de interrupción inesperados).

Se requiere mucho menos tiempo y esfuerzo para administrar Sofia2 en comparación con un desarrollo tradicional.

La administración de un despliegue de Sofia2 implica principalmente administrar configuraciones de Linux y el propio hardware; solo es necesario conocer y administrar unos pocos parámetros.

Mantenimiento y soporte técnico
-------------------------------

Las suscripciones de Sofia2 se facturan anualmente por core. Esto incluye el acceso al soporte técnico del producto, actualizaciones de software y soluciones de errores, así como ciertas funciones que solo se ofrecen en la edición de pago.

Otras ventajas de Sofia2
------------------------

Resumiendo, además de los ahorros de costes tangibles, el modelo orientado a documentos y el esquema flexible de Sofia2 también aportan mayor agilidad y flexibilidad a las empresas, que a su vez proporcionan ventajas para generar ingresos.

Una vez implantada la Plataforma Sofia2 en una empresa esta puede utilizar la Plataforma (sin necesidad de montar nueva infraestructura) para hacer nuevos desarrollos y para integrar datos de otros sistemas de forma que los tenga centralizados en un repositorio común y con capacidades Big Data. Además puede desarrollar aplicaciones Sofia2 en cualquier tecnología y lenguaje.

.. |image0| image:: ./media/image2.png
   :width: 2.15972in
   :height: 0.99167in
.. |image1| image:: ./media/image3.png
   :width: 1.40764in
   :height: 0.45556in
