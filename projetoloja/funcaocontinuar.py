def continuar():
    while True:
        print()
        print("==============================================")
        continuar = input("Deseja voltar para o sistema? (S/N): ")
        if continuar.lower() != 's' and continuar.lower() != 'n':
            print("Resposta invalida.")
        if continuar.lower() == 's':
            return True
        if continuar.lower() == 'n':
            return False