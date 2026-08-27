import re

def valor_validado(valor):
    if valor <= 0:
        return False
    else:
        return True

def produto_validado(nome):
    if nome == "":
        print("Erro: o nome do produto não pode ficar em branco.")
        return False
    elif len(nome) < 2:
        return False