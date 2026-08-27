def listar_vendas(lista_vendas):
    print("==============================================")
    for venda in lista_vendas:
        print(f"{venda['produto']} - R$ {venda['valor']:.2f}")
    print()
    print("==============================================")