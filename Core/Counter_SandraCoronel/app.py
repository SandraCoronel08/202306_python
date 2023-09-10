from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html', counter=session['counter'])

@app.route('/increment', methods=['POST'])
def increment():
    if request.form['action'] == 'increment':
        session['counter'] += 1
    elif request.form['action'] == 'reset':
        session['counter'] = 0
    return redirect(url_for('index'))

@app.route('/destroy_session')
def destroy_session():
    session.pop('counter', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
