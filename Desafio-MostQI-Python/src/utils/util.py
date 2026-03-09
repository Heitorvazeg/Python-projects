import uuid

def resolveNome(nome=None, cpf=None, nis=None):
    if nome:
        return nome
    
    if cpf:
        return f"CPF_{cpf}"
    
    if nis:
        return f"NIS_{nis}"
    
    return "DESCONHECIDO"

def generateID() -> str:
    return str(uuid.uuid4())