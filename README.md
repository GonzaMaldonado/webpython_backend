Backend SimpleMuebles
=======================

<!--
[![Lint](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/lint.yml/badge.svg?branch=master)](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/lint.yml?query=branch%3Amaster)
[![Tests](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/test.yml?query=branch%3Amaster)
-->


## Description

Implementación de autenticación y autorización de usuarios.
Con un CRUD para el apartado de muebles.


Requerimientos
-----------

* Python: "3.11.2 o >"
* Pip: "23.3.1 o >"


Empezando
-----------

- clonar el repositorio

    ```bash
    git clone https://github.com/GonzaMaldonado/webpython_backend.git
    ```

- crear un entorno virtual (en este caso lo hago con virtualenv)

    ```bash
    virtualenv -p C:\Users\AppData\Local\Programs\Python\Python311\python.exe venv
    ```

- activar entorno virtual (con Windows)

    ```bash
    venv\Scripts\activate
    ```

- instalar paquetes

    ```bash
    pip install -r requirements.txt
    ```

- Hacer las migraciones a la Base de Datos

    ```bash
    python manage.py migrate
    ```

- ejecutar el proyecto

    ```bash
    python manage.py runserver
    ```


- abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en tu navegador


### Variables de entorno
```
SECRET_KEY="secret_key_django"
DEBUG=bool
```


## Authors

Gonzalo Maldonado
<!--ex. [@GonzaMaldo](https://) -->