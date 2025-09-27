# django-prueba
Agenda de contactos en Django con CRUD

¿Para que sirve?

Esta aplicacion permite a un usuario:
1- Agregar contactos mediante nombre, correo, teléfono y direccion.
2- Listar los contactos.
3- Buscar por nombre o correo.
4- Editar y eliminar contactos.
5- Validar el formato del correo mediante EmailField y validaciones adicionales en el formulario.

Instalacion:

1-Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

2-Instalar dependencias
pip install -r requirements.txt

3-Migraciones
python manage.py migrate

4-Ejecutar servidor
python manage.py runserver

abrir en el navegador http://127.0.0.1:8000/

Estructura del proyecto
agenda-contactos/
├── agenda/                 # Proyecto Django (settings, urls, wsgi/asgi)
│   ├── settings.py         # Configuración principal del proyecto
│   └── urls.py             # Incluye rutas principales y las de la app contactos
├── contactos/              # App principal
│   ├── migrations/         
│   ├── templates/contactos/
│   │   ├── base.html           # Layout principal (Bootstrap + Icons)
│   │   ├── contact_list.html   # Vista: lista y búsqueda de contactos
│   │   ├── contact_form.html   # Vista: crear / editar contacto
│   │   └── contact_confirm_delete.html
│   ├── admin.py            # Registro del modelo Contact en admin
│   ├── forms.py            # ContactForm (validaciones adicionales)
│   ├── models.py           # Modelo Contact
│   ├── urls.py             # Rutas de la app (list, add, edit, delete)
│   └── views.py            # Vistas: contact_list, contact_create, contact_edit, contact_delete
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

Explicación de archivos

Define contact con campos:
nombre = CharField()
telefono = CharField()
email = EmailField()
direccion = CharField()

EmailField asegura validación de formato en nivel de modelo/form.

contactos/forms.py
ContactForm es ModelForm del modelo Contact. Aquí añadimos validación extra para telefono (regex que permite dígitos, +, guiones y espacios) en clean_telefono().

contactos/views.py

contact_list(request) — lista y permite búsqueda por query param q (filtra nombre__icontains y email__icontains).

contact_create(request) — maneja GET/POST para crear.

contact_edit(request, pk) — editar.

contact_delete(request, pk) — confirmación y borrado.

contactos/urls.py
Rutas:

'' → lista (contact_list)

add/ → crear (contact_create)

edit/<int:pk>/ → editar

delete/<int:pk>/ → borrar

Templates (templates/contactos/)
Usan Bootstrap y Bootstrap Icons para una UI simple y limpia. base.html contiene el navbar y la carga de CSS/Icons.

admin.py
Registro del modelo para visualizar/editar contactos desde Django Admin.