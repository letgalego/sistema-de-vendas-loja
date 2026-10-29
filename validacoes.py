def valor_validado(valor):
    if valor <= 0:
        return False
    else:
        return True

def nome_validado(nome):
    if nome == "":
        return False
    elif len(nome) < 2:
        return False
    else:
        return True

def converter_preco(preco):
    return float(preco.replace(".", ","))