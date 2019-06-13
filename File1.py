from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Mappa.html")


@app.route('/Tutte')
def index2():
    return render_template("Tutte.html")


if __name__ == '__main__':
    app.run()

