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
def home():
    # Captura os dados do formulário
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    role = request.form.get("role")

    # Adicione o print para depurar os dados recebidos
    print(f"Dados recebidos - Usuário: {usuario}, Senha: {senha}, Role: {role}")

    # Autenticação
    if autenticar_usuario(usuario, senha, role):
        if role == "residente":
            return render_template("home_residente.html")
        elif role == "professor":
            return render_template("home_professor.html")
        elif role == "gestor":
            return render_template("home_gestor.html")

    # Caso falhe a autenticação, renderiza novamente a página de login com mensagem de erro
    return render_template("home_login.html", error_message="Verifique suas credenciais!")


@app.route("/home_residente",  methods=['GET'])
def home_residente():
    return render_template("home_residente.html")


@app.route("/home_professor",  methods=['GET'])
def home_professor():
    return render_template("home_professor.html")

@app.route("/home_gestor", methods=['GET'])
def home_gestor():
    return render_template("home_gestor.html")


@app.route("/avisos_residente",  methods=['GET'])
def avisos_residente():
    return render_template("avisos_residente.html")

@app.route("/avisos_professor", methods=["GET"])
def avisos_professor():
    return render_template("avisos_professor.html")

@app.route("/notas", methods=["GET"])
def notas():
    return render_template("notas_residentes.html")


@app.route("/registrar_presenca", methods=["POST"])
def registrar_presenca():
    data = request.get_json()
    qr_code = data.get("qrcode")

    # Aqui você pode validar e registrar o QR code
    print(f"QR Code recebido: {qr_code}")

    return jsonify({"message": "Presença registrada com sucesso!"})

@app.route('/graficos', methods=["GET"])
def graficos():
    return render_template('graficos_residentes.html')

@app.route("/controle_de_residentes",  methods=['GET'])
def controle_de_residentes():
    return render_template("controle_de_residentes_professor.html")

@app.route("/lista_residentes",  methods=['GET'])
def lista_residentes():
    return render_template("lista_residentes.html")

@app.route("/lista_residentes_gestor",  methods=['GET'])
def lista_residentes_gestor():
    return render_template("lista_residentes_gestor.html")

@app.route("/rotina_professor", methods=['GET'])
def rotina_professor():
    return render_template("rotina_professor.html")

@app.route("/rotina_residente", methods=['GET'])
def rotina_residente():
    return render_template("rotina_residente.html")


if __name__ == '__main__':
    app.run(threaded=True, debug=True)