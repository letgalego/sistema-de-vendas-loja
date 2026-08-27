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
    while True:
        resp = input("Sair agora? (S/N) ")

        if resp.lower() != 's' or resp.lower() != 'n':
            print("Resposta invalida.")
        if resp.lower() == 's':
            break
        else:
            continue