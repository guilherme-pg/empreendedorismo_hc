from dbconnection import usuarios
from werkzeug.security import check_password_hash

def autenticar_usuario(usuario, senha, role):
    user = usuarios.find_one({"usuario": usuario})
    if not user:
        return False
    if not check_password_hash(user["senha"], senha):
        return False
    if user["role"] != role:
        return False
    return True
