import streamlit as st
from registrar_venda import criar_venda

def montar_tabela(vendas):
    st.session_state.tabela = []
    for venda in vendas:
        linha = {
            "Produto": venda["produto"],
            "Quantidade": venda["quantidade"],
            "Valor unitário": f"R$ {venda["valor_unitario"]:.2f}",
            "Venda total": f"R$ {venda["valor_total"]:.2f}",
        }
        st.session_state.tabela.append(linha)
    return st.session_state.tabela

def main():
    st.set_page_config(
        page_title="Caixa da loja",
        page_icon="🛒",
        layout="wide"
    )

    # Guarda as vendas entre as interações com a interface.
    if "vendas" not in st.session_state:
        st.session_state.vendas = []

    st.title("🛒 Caixa da loja")

    opcao = st.sidebar.radio(
        label="Menu",
        options=["Registrar venda", "Listar vendas"]
    )

    if opcao == "Registrar venda":
        st.subheader("Registrar venda")

        with st.form("form_venda", clear_on_submit=True):
            produto = st.text_input("Produto")

            valor = st.number_input(
                "Valor unitario (R$)",
                min_value=0.0,
                step=0.01,
                format="%.2f"
            )

            quantidade = st.number_input(
                "Quantidade",
                min_value=1.0,
                step=1.0,
                format="%0.0f"
            )

            registrar = st.form_submit_button("Registrar venda")

        if registrar:
            try:
                venda = criar_venda(produto, quantidade, valor)
            except ValueError as erro:
                st.error(str(erro))
            else:
                st.session_state.vendas.append(venda)
                st.success("Venda registrada!")

    elif opcao == "Listar vendas":
        st.subheader("Vendas registradas")

        if st.session_state.vendas:
            st.dataframe(
                montar_tabela(st.session_state.vendas)
            )
        else:
            st.info("Nenhuma venda registrada.")

    total = sum(venda["valor_total"] for venda in st.session_state.vendas)

    st.metric("Total vendido", f"R$ {total:.2f}")

if __name__ == "__main__":
    main()