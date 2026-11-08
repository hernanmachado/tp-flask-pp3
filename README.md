# TP Flask + Jinja2 - Registro de Usuarios

Aplicación web desarrollada como Trabajo Práctico para la materia **Práctica Profesionalizante 3** del **IFTS N° 18**.

El proyecto consiste en un sistema de registro de usuarios que aplica los conceptos fundamentales de Flask, el motor de plantillas Jinja2 y el procesamiento de formularios HTML.

## 🚀 Características

- **Formulario de registro** con campos para Nombre, Email, Edad, Carrera y Comentarios.
- **Validación de datos en el backend:** verifica que el nombre no esté vacío, que el email tenga un formato válido y que la edad sea un número lógico.
- **Manejo de errores:** los mensajes de validación se muestran dinámicamente en el frontend usando Jinja2, conservando los datos ya ingresados por el usuario.
- **Listado de usuarios:** vista que muestra todos los usuarios registrados en la sesión actual (almacenados en memoria).
- **Diseño institucional:** interfaz estilizada con CSS puro y el logo oficial del IFTS N° 18.

## 🛠️ Tecnologías utilizadas

- **Python 3.10**
- **Flask 3.1**
- **Jinja2 3.1**
- HTML5 & CSS3

## 📂 Estructura del proyecto

```text
tp_flask_PP3/
│
├── static/
│   └── logoIfts18.svg       # Logo institucional
│
├── templates/
│   ├── base.html            # Template base (header, nav, footer)
│   ├── formulario.html      # Vista del formulario de registro
│   ├── resultado.html       # Vista de confirmación de registro
│   └── listado.html         # Tabla con los usuarios cargados
│
├── app.py                   # Lógica principal de Flask
├── requirements.txt         # Dependencias del proyecto
└── README.md
