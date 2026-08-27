def registrar_venda():
    produto = input("Produto: ")
    valor = float(input("Valor: R$ "))

    return {
        "produto": produto,
        "valor": valor
    }