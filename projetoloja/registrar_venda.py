from validacoes import valor_validado, produto_validado

def registrar_venda():
    while True:
        try:
            produto = input("Produto: ")
            while not produto_validado(produto):
                produto = input("Produto: ")
            valor = float(input("Valor: R$ "))
            while not valor_validado(valor):
                    print("O valor deve ser maior do que zero!")
                    valor = float(input("Valor: R$ "))
        except ValueError:
             print("Digite um número válido!")
             continue
        return {
            'produto': produto,
            'valor': valor
        }