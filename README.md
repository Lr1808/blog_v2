# Blog Django

Este es un proyecto de una aplicación de Blog simple pero funcional construida con Django. Permite a los usuarios crear, leer, actualizar y eliminar (CRUD) publicaciones. También incluye autenticación de usuarios.

## Características

- **Listado de Publicaciones**: Muestra todas las publicaciones disponibles en la página de inicio.
- **Detalle de Publicación**: Vista detallada de cada publicación individual.
- **Crear Publicación**: Los usuarios autenticados pueden crear nuevas publicaciones.
- **Editar Publicación**: Funcionalidad para actualizar el contenido de las publicaciones existentes.
- **Eliminar Publicación**: Funcionalidad para eliminar publicaciones.
- **Autenticación**: Sistema de login y logout integrado.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Django**: Framework web de alto nivel.
- **SQLite**: Base de datos por defecto para desarrollo.
- **HTML/CSS**: Para las plantillas y el diseño (ubicado en `templates` y `static`).

## Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

- [Python](https://www.python.org/downloads/) (versión 3.8 o superior recomendada)
- [Git](https://git-scm.com/)

## Instalación y Configuración

Sigue estos pasos para configurar el proyecto en tu entorno local:

1.  **Clonar el repositorio**

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd Blog_Django
    ```

2.  **Crear un entorno virtual**

    Es recomendable usar un entorno virtual para manejar las dependencias.

    ```bash
    # En Windows
    python -m venv .venv
    .venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instalar dependencias**

    Instala los paquetes necesarios listados en `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

    *Nota: Si el archivo `requirements.txt` está vacío o incompleto, asegúrate de tener Django instalado:*
    ```bash
    pip install django
    ```

4.  **Realizar migraciones**

    Configura la base de datos inicial.

    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario (Opcional)**

    Para acceder al panel de administración de Django.

    ```bash
    python manage.py createsuperuser
    ```

6.  **Ejecutar el servidor de desarrollo**

    ```bash
    python manage.py runserver
    ```

    Ahora puedes acceder a la aplicación en tu navegador en `http://127.0.0.1:8000/`.

## Estructura del Proyecto

```text
Blog_Django/
├── blogs/                  # Aplicación principal del blog
│   ├── migrations/         # Migraciones de la base de datos
│   ├── models.py           # Modelos de datos (Publication)
│   ├── urls.py             # Rutas específicas de la app blogs
│   ├── views.py            # Vistas (ListView, CreateView, etc.)
│   └── ...
├── django_Project/         # Configuración del proyecto
│   ├── settings.py         # Configuraciones globales
│   ├── urls.py             # Rutas principales
│   └── wsgi.py             # Punto de entrada WSGI
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
├── templates/              # Plantillas HTML
├── db.sqlite3              # Base de datos SQLite
├── manage.py               # Script de gestión de Django
└── requirements.txt        # Dependencias del proyecto
```

## Uso

- **Inicio**: Navega a la página principal para ver las publicaciones recientes.
- **Nueva Publicación**: Haz clic en el enlace para crear una nueva publicación (requiere inicio de sesión).
- **Editar/Eliminar**: Accede a una publicación específica para ver las opciones de edición o eliminación.
- **Admin**: Accede a `/admin/` con tu superusuario para gestionar usuarios y publicaciones desde el panel de control.

## Contribución

Si deseas contribuir a este proyecto, por favor crea un *fork* del repositorio y envía un *pull request* con tus mejoras.

## Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.
