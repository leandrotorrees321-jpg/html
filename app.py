from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

contador = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/executar")
def executar():
    global contador

    contador += 1

    resposta = requests.get(
        "https://html-c0az.onrender.com/executar"
    )

    print(f"Ação executada {contador} vez(es)")

    return jsonify({
        "sucesso": resposta.ok,
        "contador": contador
    })
