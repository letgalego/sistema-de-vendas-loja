from validacoes import valor_validado, produto_validado

def registrar_venda():
    while True:
        try:
            produto = input("Produto: ")
            while not produto_validado(produto):
                produto = input("Produto: ")
            valor = float(input("Valor unitario: R$ "))
            while not valor_validado(valor):
                    print("O valor deve ser maior do que zero!")
                    valor = float(input("Valor: R$ "))
            quantidade = int(input("Quantidade: "))
            while not valor_validado(quantidade):
                    print("A quantidade deve ser maior do que zero!")
                    valor = float(input("Quantidade: "))
        except ValueError:
             print("Digite um número válido!")
             continue
        return {
            "produto": produto,
            "quantidade": quantidade,
            "valor": valor * quantidade
        }

def criar_venda(produto, quantidade, valor):
    produto = produto.strip()

    if not produto_validado(produto):
        raise ValueError("Digite um produto válido!")

    if not valor_validado(quantidade):
        raise ValueError("O valor deve ser maior do que zero!")
    
    if not valor_validado(valor):
        raise ValueError("O valor deve ser maior do que zero!")

    return {
        "produto": produto,
        "quantidade": quantidade,
        "valor_unitario": valor,
        "valor_total": valor * quantidade
    }