from dbconnection import usuarios

def autenticar_usuario(usuario, senha, role):
    # Buscar usuário com as credenciais fornecidas
    usuario_encontrado = usuarios.find_one({
        "usuario": usuario,
        "senha": senha,
        "role": role
    })
    
    # Debug: Mostra o resultado da busca
    print(f"Resultado da busca: {usuario_encontrado}")
    return usuario_encontrado is not None
