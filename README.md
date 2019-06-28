# **_Aprendizaje Automático por Refuerzo_**

**Inteligencia Artificial 2018/19**

Desarrollado por **Alejandro Rodríguez Romero** y **Carlos Campos Cuesta**.

Este proyecto esta desarollado en `Python  3`.

El proyecto es accesible desde [http://qlearning.pomosoft.com/](http://qlearning.pomosoft.com/). Si se desea probar en local se recomienda seguir los siguientes pasos:

# Estructura del proyecto

Dado que el proyecto esta basado en una aplicación web en [Django](https://www.djangoproject.com/) esta organizado con la siguiente estructura:

    q-learning
    ├── aux
    │   └── numpy_encoder.py
    ├── docker-compose.yml
    ├── docker-entrypoint.sh
    ├── Dockerfile
    ├── manage.py
    ├── qlearning
    │   ├── enviroment.py
    │   └── qlearning.py
    ├── qlearning_app
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   ├── models.py
    │   ├── templatetags
    │   │   └── util_tags.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── qlearning_project
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── README.md
    ├── requirements.txt
    ├── static
    │   ├── css
    │   ├── images
    │   └── js
    └── templates
        └── app

A continuación detallamos los directorios más importantes:

* *qlearning:* En este directorio se encuentra todo lo referente al algoritmo de Q-Learning. Se compone de los ficheros `enviroment.py` y `qlearning.py`.

    * `enviroment.py`: En este fichero se detallan la clase `Enviroment` que esta compuesta por todos los métodos necesarios para la creación del entorno.
        * reset
        * step
        * random_action
        * render

    * `qlearning.py`:En este fichero se detallan la clase `Qlearning` que esta compuesta por todos los métodos necesarios para la creación del problema.
        * _render
        * call

* *qlearning_app:* En este directorio se encuentrann los ficheros necesarios para el correcto funcionamiento de la aplicación. En ella se definen los modelos de los que hace uso la aplicación así como formularios y vistas.

* *qlearning_project:* En este directorio se encuentran los ficheros necesarios para la configuración de la aplicación.

# Instalación

Para un buen funcionamiento del proyecto se recomienda el uso de un espacio virtual ([virtualenv](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)), una vez configurado el entorno es necesario que se instalen los requisitos para abrimos una terminal en la raíz del proyecto y pondremos:

    $ pip install -r requirements.txt

Tras configurar el entorno pasaremos a configurar el proyecto para poderlo ejecutar.

# Puesta en marcha

Desde el directorio raíz del proyecto tendremos que ejecutar las siguientes instrucciones:

    $ python manage.py migrate

    $ python manage.py runserver

Este última instrucción nos levantará el servidor de Django para poder ver la aplicación. Accedemos a [localhost:8000](http://localhost:8000/) desde el navegador y podremos hacer uso de la aplicación. Para ello le recomendamos seguir la guía de la propia página.

## Recomendaciones

* Uso del navegador Google Chrome
* Habilitar el uso de JavaScript del navegador
* Se recomienda el uso en la aplicación desplegada: [http://qlearning.pomosoft.com/](http://qlearning.pomosoft.com/)

## Contacto

Si necesita alguna aclaración para el uso de la aplicación puede contactar con nosotros a traves de nuestros correos personales:

* Alejandro Rodríguez Romero - alerodri1994@gmail.com
* Carlos Campos Cuesta - carcamcue@gmail.com