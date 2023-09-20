from flask_app import app
# ...server.py

from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo para la vista
users = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@example.com'}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
