
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/",  methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/login_form", methods=['POST'])
def login_form():

    # return render_template("comparison.html", rendering=metrics)
    # return render_template("home_professor.html")
    return render_template("home_residente.html")


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
