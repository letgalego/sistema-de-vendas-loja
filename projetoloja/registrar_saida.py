from validacoes import valor_validado

def registrar_saida():
        while True:
                try:
                        saida = input("Nome da saida: ")
                        valor = float(input("Valor: R$ "))
                        while not valor_validado(valor):
                                print("O valor deve ser maior do que zero!")
                                valor = float(input("Valor: R$ "))
                except ValueError:
                        print("Digite um número válido.")
                return {
                        "nome": saida,
                        "valor": valor
                }