def registrar_saida():
    saida = input("Nome da saida: ")
    valor = float(input("Valor: R$ "))
    return {
        "nome": saida,
        "valor": valor
    }