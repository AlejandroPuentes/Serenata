from flask import Flask, render_template, url_for, redirect
from Banda import Banda

app = Flask(__name__)


banda = Banda()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/construir/')
def home():
    banda.construirBanda()
    return render_template('construir.html', musicos=banda.getCantidad())


@app.route('/construir/preparar/')
def preparar():
    return render_template('alistar.html', instrumentos=banda.getInstrumentos())

@app.route('/construir/tocar/')
def tocarSerenata():
    return render_template('tocar.html', instrumentos=banda.getInstrumentos())

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
