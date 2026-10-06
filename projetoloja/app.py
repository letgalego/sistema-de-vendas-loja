import streamlit as st
from formularios import criar_venda, formulario_venda, formulario_saida, criar_saida

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

    # Guarda as vendas entre as interações com a interface.
    if "vendas" not in st.session_state:
        st.session_state.vendas = []
    if "saidas" not in st.session_state:
        st.session_state.saidas = []

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
        produto, quantidade, valor, registrar = formulario_venda()

        if registrar:
            try:
                venda = criar_venda(produto, quantidade, valor)
            except ValueError as erro:
                st.error(str(erro))
            else:
                st.session_state.vendas.append(venda)
                st.success("Venda registrada!")

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
            st.dataframe(
                montar_tabela_vendas(st.session_state.vendas)
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