from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask import Forms, StringField, SubmitField, PasswordField
from wtforms.fields import DataRequired

app = Flask(__name__)
Bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar cafe', 'Solicitud de compra', 'Entregar video al productor']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip

    return response

@app.route('/hello')
def hello():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')

    # response_string = f'''Flask says: Kicite Joloche!\n
    # tu IP es esta {user_ip}. ZAZ!''' 
    
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
        'login_form' : login_form
    }

    return render_template('hello.html', **context)