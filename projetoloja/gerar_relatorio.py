def gerar_relatorio(lista_vendas, lista_saidas):
    if len(lista_vendas) > 0:
        print()
        print("==============================================")
        print("                   VENDAS                     ")
        print("==============================================")
        for venda in lista_vendas:
            print(f"{venda['produto']} | R$ {venda['valor']}")
    if len(lista_saidas) > 0:
        print("==============================================")
        print("                     ...                      ")
        print("==============================================")
        print("                   SAIDAS                     ")
        print("==============================================")
        for saida in lista_saidas:
            print(f"{saida['nome']} | R$ {saida['valor']}")
        print("==============================================")
        print()
    caixa_total = sum(venda['valor'] for venda in lista_vendas) - sum(saida['valor'] for saida in lista_saidas)
    print(f"Caixa total de hoje: R$ {caixa_total:.2f}")
    return caixa_total