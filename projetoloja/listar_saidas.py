def listar_saidas(lista_saidas):
    print()
    print("==============================================")
    for saida in lista_saidas:
        print(f"{saida['nome']} - R$ {saida['valor']:.2f}")
    total = sum(saida['valor'] for saida in lista_saidas)
    print("==============================================")
    print()
    print(f"Total: R$ {total}")
    print("==============================================")
    print()