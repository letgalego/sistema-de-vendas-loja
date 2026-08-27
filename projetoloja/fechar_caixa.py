def fechar_caixa(lista_vendas, lista_saidas):

    total_vendas = sum(lista_vendas['valor'] for venda in lista_vendas)
    total_saidas = sum(lista_saidas['valor'] for saida in lista_saidas)
    saldo = total_vendas - total_saidas

    print("==============================================")
    print("                 FECHAMENTO                   ")
    print()
    print(f"Vendas: {total_vendas:.2f}")
    print(f"Saidas: {total_saidas:.2f}")
    print(f"---------------------------------------------")
    print(f"Saldo do dia: {saldo:.2f}")
    return saldo