from flask import Flask, render_template,url_for , redirect
from Banda import Banda

app = Flask(__name__)

@app.route('/')
def index():
    banda = Banda()
    banda.construirBanda()
    x = banda.cantidad()
    y = banda.getInstrumentos()
    return render_template('index.html',musicos=x, instrumento=y)



if __name__ == '__main__':
    app.run(debug=True)