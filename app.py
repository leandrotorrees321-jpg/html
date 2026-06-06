from flask import Flask, render_template, jsonify
import webbrowser
import threading
import time

app = Flask(__name__)

contador = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/executar")
def executar():
    global contador

    contador += 1
    webbrowser.open("https://html-c0az.onrender.com/")
    print(f"Ação executada {contador} vez(es)")
    
    return jsonify({
        "sucesso": True,
        "contador": contador
    })

def abrir_navegador():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=abrir_navegador).start()
    app.run(debug=False)
