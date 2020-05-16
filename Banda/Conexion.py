from flask import Flask, render_template,url_for , redirect
from Banda import Banda

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('LLamarM.html')

@app.route('/construir/')
def LLamarM():
    banda = Banda()
    x = banda.cantidad()
    return render_template('index.html',musicos=x)

@app.route('/construir/prepara/')
def Preparar():
    banda = Banda()
    banda.construirBanda()
    x = banda.cantidad()
    y = banda.getInstrumentos()
    return render_template('Alistar.html',musicos=x, instrumento=y)

if __name__ == '__main__':
    app.run(debug=True)