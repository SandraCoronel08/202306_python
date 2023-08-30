from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('index.html')

@app.route('/play/<int:x>/<color>')
def mostrar_cajas_color(x, color):
    return render_template('index.html', num_cajas=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)
