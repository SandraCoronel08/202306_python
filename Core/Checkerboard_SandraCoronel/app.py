from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chessboard_default():
    return render_template('chessboard.html', rows=8, cols=8)

@app.route('/<int:x>')
def chessboard_custom_rows(x):
    return render_template('chessboard.html', rows=x, cols=8)

@app.route('/<int:x>/<int:y>')
def chessboard_custom_rows_cols(x, y):
    return render_template('chessboard.html', rows=x, cols=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def chessboard_custom_colors(x, y, color1, color2):
    return render_template('chessboard.html', rows=x, cols=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=False)
