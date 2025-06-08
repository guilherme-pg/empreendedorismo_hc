from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, jsonify
from auth import autenticar_usuario
from config import Config # <-- Importe sua classe de configuração

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=['GET'])
def home_login():
    return render_template("home_login.html")

@app.route("/home", methods=['POST'])
def login_form():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    role = request.form.get("role")

    if autenticar_usuario(usuario, senha, role):
        if role == "residente":
            return render_template("home_residente.html")
        elif role == "professor":
            return render_template("home_professor.html")
        elif role == "gestor":
            return render_template("home_gestor.html")
    # Caso falhe a autenticação, renderiza novamente a página de login e passa a mensagem de erro
    return render_template("home_login.html", error_message="Verifique suas credenciais!")



@app.route("/home_residente",  methods=['GET'])
def home_residente():
    return render_template("home_residente.html")


@app.route("/home_professor",  methods=['GET'])
def home_professor():
    return render_template("home_professor.html")


@app.route("/avisos",  methods=['GET'])
def avisos():
    return render_template("avisos.html")


@app.route("/ponto_residente",  methods=['GET'])
def ponto_residente():
    return render_template("ponto_residente.html")


@app.route("/controle_de_residentes",  methods=['GET'])
def controle_de_residentes():
    return render_template("controle_de_residentes_professor.html")

@app.route("/lista_residentes",  methods=['GET'])
def lista_residentes():
    return render_template("lista_residentes.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
