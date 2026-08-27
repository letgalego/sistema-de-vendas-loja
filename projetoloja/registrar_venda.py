from validacoes import valor_validado, nome_validado

def registrar_venda():
    produto = input("Produto: ")
    while not nome_validado(produto):
          print("Nome invalido!")
          produto = input("Produto: ")
    valor = float(input("Valor: R$ "))
    while not valor_validado(valor):
            print("O valor deve ser maior do que zero!")
            valor = float(input("Valor: R$ "))
    return {
        "produto": produto,
        "valor": valor
    }