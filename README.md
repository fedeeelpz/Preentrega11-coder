# Blog Django

Blog desarrollado con Django, con sistema de posts (CRUD completo), imágenes asociadas, autenticación de usuarios y perfiles personalizados.

## Funcionalidades

- Páginas estáticas: Inicio y Acerca de
- Listado de posts publicados
- Vista de detalle individual por post
- Crear nuevo post (con imagen opcional)
- Editar post existente (incluyendo cambio de imagen)
- Eliminar post (con página de confirmación previa)
- Sistema de autenticación (Login y Logout)
- Registro de usuarios con formulario personalizado
- Perfil de usuario con relación OneToOne, biografía y avatar personalizable
- Protección de vistas CRUD (crear, editar, eliminar) para usuarios autenticados
- Navegación dinámica según el estado de sesión del usuario
- Panel de administración de Django

## Tecnologías

- Python
- Django
- SQLite (base de datos local)
- Pillow (procesamiento de imágenes)
- HTML / CSS

## Instalación

1. Cloná el repositorio

```
git clone https://github.com/fedeelpz/Preentrega10-coder
cd Preentrega10-coder
```

2. Creá y activá un entorno virtual

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

3. Instalá las dependencias

```
pip install -r requirements.txt
```

4. Aplicá las migraciones

```
python manage.py migrate
```

5. Creá un superusuario (para acceder al panel de administración)

```
python manage.py createsuperuser
```

6. Corré el servidor

```
python manage.py runserver
```

7. Accedé a la aplicación

- Inicio: http://127.0.0.1:8000/inicio/
- Acerca de: http://127.0.0.1:8000/acerca/
- Posts: http://127.0.0.1:8000/posts/
- Iniciar sesión: http://127.0.0.1:8000/accounts/login/
- Registrarse: http://127.0.0.1:8000/accounts/registro/
- Perfil: http://127.0.0.1:8000/accounts/perfil/
- Panel de administración: http://127.0.0.1:8000/admin/

## Operaciones CRUD disponibles

| Operación | URL |
|---|---|
| Listar posts | `/posts/` |
| Ver detalle de un post | `/posts/<id>/` |
| Crear un post | `/posts/crear/` |
| Editar un post | `/posts/<id>/editar/` |
| Eliminar un post | `/posts/<id>/eliminar/` |

## Manejo de imágenes y Perfiles

- Cada post puede tener una imagen asociada (campo `imagen`, opcional).
- Cada usuario cuenta con un perfil asociado (`Perfil`) con campos para **biografía** y **avatar**.
- Se utiliza la librería **Pillow** para el procesamiento de imágenes (dependencia instalada con `pip install Pillow`).
- Las imágenes se guardan en la carpeta `media/` (con subcarpetas `media/posts/` y perfiles), configurada mediante `MEDIA_URL` y `MEDIA_ROOT` en `settings.py`.
- Durante el desarrollo, las imágenes se sirven agregando la configuración de `static()` en `blog_project/urls.py`, activa solo cuando `DEBUG = True`.

### Cómo probar la carga de archivos

1. Entrá a `/accounts/registro/` para crear una cuenta propia o iniciá sesión.
2. Ingresá a tu perfil (`/accounts/perfil/`) o editá tus datos para subir un avatar y actualizar tu biografía.
3. Entrá a `/posts/crear/` o editá un post existente para asociarle una imagen.
4. Guardá el formulario y verificá que la imagen y el avatar se muestren correctamente en la interfaz.

## Estructura del proyecto

```text
blog_consola/
├── manage.py
├── blog_project/           # Configuración del proyecto
│   ├── settings.py
│   └── urls.py
├── accounts/               # App de usuarios y perfiles
│   ├── models.py           # Modelo Perfil (OneToOne con User)
│   ├── views.py            # Vistas de registro, perfil y edición
│   ├── forms.py            # Formulario de registro y perfil
│   ├── urls.py             # Rutas de autenticación
│   └── templates/          # Plantillas de login, registro y perfil
├── posts/                  # App principal de blog
│   ├── models.py           # Modelo Post
│   ├── views.py            # Lógica del CRUD
│   ├── forms.py            # Formulario de posts (con soporte de imágenes)
│   ├── urls.py             # Rutas de la app
│   ├── admin.py            # Configuración del panel admin
│   ├── templates/          # Templates HTML de posts
│   └── static/             # Archivos CSS
└── media/                  # Imágenes subidas por los usuarios (posts y avatares)
```