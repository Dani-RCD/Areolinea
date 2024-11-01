from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, IntegerField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TimeField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ReservaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    salida = StringField('Salida de', validators=[DataRequired()])
    fecha_salida = DateField('Fecha de salida', format='%Y-%m-%d', validators=[DataRequired()])
    hora_salida = TimeField('Hora de salida', validators=[DataRequired()])
    modo_vuelo = SelectField('Modo de vuelo', choices=[('redondo', 'Redondo'), ('solo', 'Solo vuelo')], validators=[DataRequired()])
    llegada = StringField('Llegada a', validators=[DataRequired()])
    fecha_llegada = DateField('Fecha de llegada', format='%Y-%m-%d', validators=[DataRequired()])
    

    submit = SubmitField('Enviar Reserva')


class VueloForm(FlaskForm):
    operador = StringField('Operador', validators=[DataRequired()])
    matricula = StringField('Matrícula del avión', validators=[DataRequired()])
    precio = IntegerField('Precio', validators=[DataRequired()])
    salida = StringField('Salida de', validators=[DataRequired()])
    fecha_salida = DateField('Fecha de salida', format='%Y-%m-%d', validators=[DataRequired()])
    hora_salida = TimeField('Hora de salida', validators=[DataRequired()])
    tipo_vuelo = SelectField('Tipo de vuelo', choices=[('privado', 'Privado'), ('comercial', 'Comercial')], validators=[DataRequired()])
    llegada = StringField('Llegada a', validators=[DataRequired()])
    fecha_llegada = DateField('Fecha de llegada', format='%Y-%m-%d', validators=[DataRequired()])
    modo_vuelo = SelectField('Modo de vuelo', choices=[('redondo', 'Redondo'), ('solo', 'Solo vuelo')], validators=[DataRequired()])
    
    submit = SubmitField('Agregar Vuelo')


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    correo = EmailField('Correo Electrónico', validators=[DataRequired(), Email()])
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Crear Cuenta')
