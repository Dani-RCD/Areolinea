from flask import Flask, render_template, redirect, url_for, flash, session
from forms import VueloForm, ReservaForm, LoginForm, RegistroForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto a una clave segura en producción

reservas = []  # Lista global para almacenar reservas
vuelos = []    # Lista global para almacenar vuelos

# Datos de usuarios de ejemplo (en producción, usa una base de datos)
usuarios = {
    "admin": generate_password_hash("password123"),  # Guardar contraseña hasheada
    "usuario": generate_password_hash("mi_contraseña")  # Guardar contraseña hasheada
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Verifica la contraseña usando check_password_hash
        if username in usuarios and check_password_hash(usuarios[username], password):
            session['username'] = username
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('iniciar_sesion.html', form=form)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Aquí puedes agregar lógica para guardar el nuevo usuario en una base de datos
        if username not in usuarios:
            usuarios[username] = generate_password_hash(password)  # Almacena la contraseña hasheada
            flash('¡Registro exitoso! Puedes iniciar sesión ahora.', 'success')
            return redirect(url_for('iniciar_sesion'))
        else:
            flash('El nombre de usuario ya está en uso. Elige otro.', 'danger')

    return render_template('registro.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Por favor inicia sesión primero.', 'warning')
        return redirect(url_for('iniciar_sesion'))
    
    return render_template('dashboard.html')

@app.route('/gestionar_reserva', methods=['GET', 'POST'])
def gestionar_reservas():
    form = ReservaForm()
    if form.validate_on_submit():
        # Lógica para guardar la reserva
        flash('Reserva guardada con éxito!', 'success')
        return redirect(url_for('gestionar_reserva'))

    return render_template('gestionar_reserva.html', form=form)

@app.route('/gestionar_vuelos', methods=['GET', 'POST'])
def gestionar_vuelos():
    form = VueloForm()
    if form.validate_on_submit():
        # Lógica para guardar el vuelo
        flash('Vuelo agregado con éxito!', 'success')
        return redirect(url_for('gestionar_vuelos'))

    return render_template('gestionar_vuelos.html', form=form)



@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.pop('username', None)
    flash('¡Has cerrado sesión exitosamente!', 'success')
    return redirect(url_for('iniciar_sesion'))

if __name__ == '__main__':
    app.run(debug=True)
