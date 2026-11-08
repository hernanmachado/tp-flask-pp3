from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Almacenamiento en memoria (para el desafío integrador)
usuarios = []

# Regex simple para validar email
EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')


@app.route('/', methods=['GET', 'POST'])
def formulario():
    errores = {}
    datos = {}

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        edad = request.form.get('edad', '').strip()
        carrera = request.form.get('carrera', '').strip()
        comentarios = request.form.get('comentarios', '').strip()

        # Guardamos para repoblar el form si hay errores
        datos = {
            'nombre': nombre,
            'email': email,
            'edad': edad,
            'carrera': carrera,
            'comentarios': comentarios,
        }

        # --- Actividad 1: Validaciones ---
        if not nombre:
            errores['nombre'] = 'El nombre no puede estar vacío.'

        if not email:
            errores['email'] = 'El email es obligatorio.'
        elif not EMAIL_REGEX.match(email):
            errores['email'] = 'El formato del email no es válido.'

        if not edad:
            errores['edad'] = 'La edad es obligatoria.'
        elif not edad.isdigit():
            errores['edad'] = 'La edad debe ser un número.'
        elif not (1 <= int(edad) <= 120):
            errores['edad'] = 'La edad debe estar entre 1 y 120.'

        if not carrera:
            errores['carrera'] = 'Debe seleccionar una carrera.'

        # --- Si no hay errores: guardar usuario ---
        if not errores:
            usuarios.append({
                'nombre': nombre,
                'email': email,
                'edad': int(edad),
                'carrera': carrera,
                'comentarios': comentarios,
            })
            return render_template(
                'resultado.html',
                nombre=nombre,
                email=email,
                edad=edad,
                carrera=carrera,
                comentarios=comentarios,
            )

    # GET o POST con errores
    return render_template(
        'formulario.html',
        errores=errores,
        datos=datos,
        carreras=['TSDS', 'TSCDIA', 'TSAS'],
    )


@app.route('/usuarios')
def listado():
    return render_template('listado.html', usuarios=usuarios)


if __name__ == '__main__':
    app.run(debug=True)