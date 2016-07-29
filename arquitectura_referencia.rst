.. figure::  ./images/logo_sofia2_grande.png
 :align:   center
 
Arquitectura de Referencia
==========================

Componentes de Despliegue
-------------------------

Los componentes de Sofia2 son:

* **SIB Runtime**: Es el core de la plataforma, encargado de procesar y almacenar todos los mensajes recibidos por Sofia2. Expone interfaces (MQTT, WebSockets, REST,…) para que los clientes puedan publicar y consultar información.
* **Web Console**: Consola Web + API Web para gestionar/administrar la plataforma. Facilita el modo de configurar Sofia2
* **API Manager**: Permite exponer la información de negocio del dominio de Sofia2 mediante APIs REST. Asimismo, puede actuar de punto centralizador de invocación a otras APIs REST externas.
* **SIB Tools (Script)**: Es el módulo que proporciona capacidad de ejecución de reglas Script y CEP.
* **SIB Tools (Proccess)**: Es el módulo encargado de realizar procesos en backgroud en la plataforma Sofia2, entre ellos, paso de información de BDTR a BDH, limpieza de registro de log de procesos. Borrado de información en BDTR que ha dejado de pertenecer a la ventana de tiempo real.
* **Contenedor KP’s**: Proporciona un entorno para la ejecución de determinados KPs pertenecientes a usuarios privilegiados de la plataforma Sofia2.
* **BDC**: Almacena toda la información de onfiguración de la Plataforma. Puede ser cualquier BD relacional con driver JDBC. Actulamente Sofia2 está certificada sobre MySQL y Oracle. 
* **BDTR**: Almacena los datos del tiempo real de las Apps que utilizan la plantaforma. La implementación de referencia está certificada sobre MongoDB, aunque con las limitaciones impuestas por las propias bases de datos, se pueden soportar cualquier BD relacional con  driver JDBC.
* **BDH**: Almacena la información de la plataforma que ha dejado de pertenecer a la ventana de tiempo real y se considera como información histórica. Se soporta sobre infraestructura Hadoop.

En una instalación de Sofia2 no es necesario instalar todos los módulos, ya que cada módulo cubre un conjunto de funcionalidades bien diferenciadas. Dependerá de cada caso concreto que módulos se instalan en la instalación de Sofia2.

Cada módulo Sofia2 puede funcionar en instancia única o en cluster, dependiendo de la carga de trabajo a la que se vaya a someter.

Plugins
-------

Los  plugins son componentes que, añaden una funcionalidad adicional o una nueva característica a la  platafoma, sin tener que modificar el core de la misma.
Los plugins se empaquetan como fichersos JAR (Java Application Resource), cuyas cláses se incluirán en tiempo de ejecución, junto con el resto de clases del core de la plataforma, añadiendo de este modo  nuevas funcionalidades..

Existen distintos tipos de plugins:

* **Seguridad**: Permiten personalizar el mecanismo de autenticación/autorización en los módulos de Sofia2, adaptándose al módelo existente en la organización donde se despliega Sofia2. 
*	**Plugin-Gateway**: Permiten añadir nuevos protocolos e interfaces de comunicación para el envio/recepción de información desde/hacia Sofia2
* **Plugins de pre/post procesado**: Permiten realizar ciertas acciones con un mensaje recibido por la plataforma antes y/o después de ser procesado
*	**Plugins de plataforma**: Son plugins desarrollados a medida para  Sofia2. Realizan funciones de integración entre componentes de la plataforma.

