from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Got Post Info")
        session['username'] = request.form['name']
        session['useremail'] = request.form['email']
        return redirect('/show')
    return render_template("index.html")

@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)
