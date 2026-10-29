import streamlit as st
from formularios import formulario_venda, formulario_pagamento,formulario_saida,criar_saida,resumo_pagamento, registrar_e_limpar

def montar_tabela_vendas(vendas):
    tabela = []
    for venda in vendas:
        linha = {
            "Produto": venda["produto"],
            "Quantidade": venda["quantidade"],
            "Valor unitário": f"R$ {venda["valor_unitario"]:.2f}",
            "Venda total": f"R$ {venda["valor_total"]:.2f}",
        }
        tabela.append(linha)
    return tabela

def montar_tabela_saida(saidas):
    tabela = []
    for saida in saidas:
        linha = {
            "Descrição": saida["descricao"],
            "Valor": f"R$ {saida["valor"]:.2f}",
        }
        tabela.append(linha)
    return tabela

def main():
    st.set_page_config(
        page_title="Caixa da loja",
        page_icon="🛒",
        layout="wide"
    )

    # guarda as listas durante as interaçoes na interface
    if "vendas" not in st.session_state:
        st.session_state.vendas = []
    if "saidas" not in st.session_state:
        st.session_state.saidas = []
    if "carrinho" not in st.session_state:
        st.session_state.carrinho = []

    rotulos = {
        "Registrar venda": "🛒 Registrar venda",
        "Registrar saída": "💸 Registrar saída",
        "Relatorio do dia": "🗓️ Relatorio do dia"
    }

    st.title("🛒 Caixa da loja")

    resumo = st.container()

    st.divider()

    with st.sidebar:
        st.title("Gestão da loja")
        opcao = st.sidebar.radio(
            "Menu",
            options=list(rotulos),
            format_func=lambda opcao: rotulos[opcao]
        )

    if opcao == "Registrar venda":
        col_formulario, col_resumo = st.columns([2, 1])

        with col_formulario:
            formulario_venda()

            st.subheader("Itens da compra")

            if st.session_state.carrinho:
                st.dataframe(
                    montar_tabela_vendas(st.session_state.carrinho),
                    hide_index=True
                )
            else:
                st.info("Nenhum item no carrinho.")

        total_compra = sum(
            item["valor_total"]
            for item in st.session_state.carrinho
        )

        with col_resumo:
            with st.container(border=True):
                pagamento, recebido = formulario_pagamento()

                st.divider()

                resumo_pagamento(
                    pagamento,
                    total_compra,
                    recebido
                )

                st.button(
                    "Finalizar venda",
                    key="finalizar_venda",
                    on_click=registrar_e_limpar,
                    disabled=not st.session_state.carrinho
                )

        mensagem = st.session_state.pop("mensagem_venda", None)

        if mensagem is not None:
            tipo, texto = mensagem

            if tipo == "sucesso":
                st.success(texto)
            else:
                st.error(texto)

    elif opcao == "Registrar saída":
        descricao, valor, registrar = formulario_saida()

        if registrar:
            try:
                saida = criar_saida(descricao, valor)
            except ValueError as erro:
                st.error(str(erro))
            else:
                st.session_state.saidas.append(saida)
                st.success("Saída registrada!")

    elif opcao == "Relatorio do dia":
        st.subheader("Vendas registradas")

        if st.session_state.vendas:
            for numero, venda in enumerate(
                st.session_state.vendas,
                start=1
            ):
                titulo = (
                    f"Venda {numero} — "
                    f"R$ {venda['valor_total']:.2f}"
                )

                with st.expander(titulo):
                    itens = venda.get("itens", [venda])

                    st.dataframe(
                        montar_tabela_vendas(itens),
                        hide_index=True
                    )

                    pagamento = venda.get("forma_pagamento")

                    if pagamento is not None:
                        st.write(f"Pagamento: {pagamento}")

                    if pagamento == "Dinheiro":
                        st.write(
                            f"Recebido: R$ {venda['recebido']:.2f}"
                        )
                        st.write(
                            f"Troco: R$ {venda['troco']:.2f}"
                        )
        else:
            st.info("Nenhuma venda registrada.")

        st.divider()

        st.subheader("Saídas registradas")
        
        if st.session_state.saidas:
            st.dataframe(
                montar_tabela_saida(st.session_state.saidas)
            )
        else:
            st.info("Nenhuma saída registrada.")

    venda_total = sum(venda["valor_total"] for venda in st.session_state.vendas)
    saida_total = sum(saida["valor"] for saida in st.session_state.saidas)
    caixa_total = venda_total - saida_total

    with resumo:
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Caixa do dia", value=f"R$ {caixa_total:.2f}")
        col2.metric(label="Total vendas", value=f"R$ {venda_total:.2f}")
        col3.metric(label="Total saídas", value=f"R$ {saida_total:.2f}")

if __name__ == "__main__":
    main()