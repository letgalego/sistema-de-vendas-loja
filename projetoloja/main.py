from registrar_venda import registrar_venda
from registrar_saida import registrar_saida
from listar_vendas import listar_vendas
from listar_saidas import listar_saidas
from gerar_relatorio import gerar_relatorio
from funcaocontinuar import continuar
from fechar_caixa import fechar_caixa

vendas = []
saidas = []
caixa_final = 0

while True:
    print("==============================================")
    print("                   SISTEMA                    ")
    print("==============================================")
    print("1 - Registrar venda")
    print("2 - Registrar saída")
    print("3 - Listar vendas")
    print("4 - Listar saídas")
    print("5 - Relatório do dia")
    print("6 - Fechar caixa")
    print("==============================================")
    print()
    print("==============================================")
    resp = int(input("Digite sua resposta: "))

    if resp == 1:
        while True:
            vendas.append(registrar_venda())
            if continuar():
                break
    elif resp == 2:
        while True:
            saidas.append(registrar_saida())
            if continuar():
                break
    elif resp == 3:
        if len(vendas) > 0:
            while True:
                listar_vendas(vendas)
                if continuar():
                    break
        else:
            print("Voce nao adicionou nenhuma venda!")
    elif resp == 4:
        if len(saidas) > 0:
            while True:
                listar_saidas(saidas)
                if continuar():
                    break
        else:
            print("Voce nao adicionou nenhuma saida!")
    elif resp == 5:
        if len(saidas) > 0 or len(vendas) > 0:
            gerar_relatorio(vendas, saidas)
        else:
            print("Voce nao adicionou nenhuma venda ou saida!")
    elif resp == 6:
        caixa_total = fechar_caixa(vendas, saidas)
        break
    else:
        print("Resposta inválida!")