from validacoes import valor_validado, nome_validado
import streamlit as st

def formulario_venda():
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
        return produto, quantidade, valor, registrar

def formulario_saida():
    st.subheader("Registrar saida")

    with st.form("form_venda", clear_on_submit=True):
        descricao = st.text_input("Descrição da saída")
        valor = st.number_input(
            "Valor (R$)",
            min_value=0.0,
            step=0.01,
            format="%.2f"
        )
        registrar = st.form_submit_button("Registrar saída")
        return descricao, valor, registrar


def criar_venda(produto, quantidade, valor):
    produto = produto.strip()

    if not nome_validado(produto):
        raise ValueError("Digite um produto válido!")

    if not valor_validado(quantidade):
        raise ValueError("O valor deve ser maior do que zero!")
    
    if not valor_validado(valor):
        raise ValueError("O valor deve ser maior do que zero!")

    return {
        "produto": produto,
        "quantidade": quantidade,
        "valor_unitario": valor,
        "valor_total": valor * quantidade
    }

def criar_saida(descricao, valor):
    descricao = descricao.strip()

    if not nome_validado(descricao):
        raise ValueError("Digite um produto válido!")
    
    if not valor_validado(valor):
        raise ValueError("O valor deve ser maior do que zero!")

    return {
        "descricao": descricao,
        "valor": valor
    }