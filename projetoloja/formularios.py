from validacoes import valor_validado, nome_validado
import streamlit as st

def formulario_venda():
    with st.container(border=True):
        st.subheader("Adicionar item à compra")

        st.text_input("Produto", key="venda_produto")

        col1, col2 = st.columns(2)

        with col1:
            st.number_input(
                "Valor unitário (R$)",
                min_value=0.0,
                step=0.01,
                format="%.2f",
                key="venda_valor"
            )

        with col2:
            st.number_input(
                "Quantidade",
                min_value=1,
                step=1,
                key="venda_quantidade"
            )

        total_item = (
            st.session_state.venda_quantidade
            * st.session_state.venda_valor
        )

        st.write(f"**Total deste item: R$ {total_item:.2f}**")

        st.button(
            "Adicionar item",
            key="adicionar_item",
            on_click=adicionar_e_limpar
        )

def criar_item(produto, quantidade, valor):
    produto = produto.strip()

    if not nome_validado(produto):
        raise ValueError("Digite um produto válido!")

    if quantidade <= 0 or quantidade != int(quantidade):
        raise ValueError("A quantidade deve ser um inteiro maior que zero!")

    if not valor_validado(valor):
        raise ValueError("O valor unitário deve ser maior que zero!")

    return {
        "produto": produto,
        "quantidade": quantidade,
        "valor_unitario": valor,
        "valor_total": quantidade * valor
    }


def criar_venda(itens, pagamento, recebido=None):
    if not itens:
        raise ValueError("Adicione pelo menos um item!")

    if pagamento not in ["Dinheiro", "Pix", "Cartão"]:
        raise ValueError("Selecione uma forma de pagamento válida!")

    total = sum(item["valor_total"] for item in itens)
    troco = None

    if pagamento == "Dinheiro":
        if recebido is None or recebido < total:
            raise ValueError("O valor recebido deve cobrir a compra!")

        troco = round(recebido - total, 2)
    else:
        recebido = None

    return {
        "itens": [item.copy() for item in itens],
        "valor_total": total,
        "forma_pagamento": pagamento,
        "recebido": recebido,
        "troco": troco
    }

def adicionar_e_limpar():
    try:
        item = criar_item(
            st.session_state.venda_produto,
            st.session_state.venda_quantidade,
            st.session_state.venda_valor
        )
    except ValueError as erro:
        st.session_state.mensagem_venda = ("erro", str(erro))
    else:
        st.session_state.carrinho.append(item)

        # Limpa somente os campos do item.
        st.session_state.venda_produto = ""
        st.session_state.venda_quantidade = 1
        st.session_state.venda_valor = 0.0

        st.session_state.mensagem_venda = (
            "sucesso", "Item adicionado ao carrinho!"
        )


def formulario_pagamento():
    pagamento = st.radio(
        "Forma de pagamento",
        options=["Dinheiro", "Pix", "Cartão"],
        horizontal=True,
        key="venda_pagamento"
    )

    recebido = None

    if pagamento == "Dinheiro":
        recebido = st.number_input(
            "Valor recebido (R$)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            key="venda_recebido"
        )

    return pagamento, recebido

def registrar_e_limpar():
    try:
        venda = criar_venda(
            st.session_state.carrinho,
            st.session_state.venda_pagamento,
            st.session_state.get("venda_recebido")
        )
    except ValueError as erro:
        st.session_state.mensagem_venda = ("erro", str(erro))
    else:
        st.session_state.vendas.append(venda)

        # Limpa a compra apenas depois de finalizar com sucesso.
        st.session_state.carrinho = []

        st.session_state.venda_produto = ""
        st.session_state.venda_quantidade = 1
        st.session_state.venda_valor = 0.0
        st.session_state.venda_pagamento = "Dinheiro"
        st.session_state.venda_recebido = 0.0

        st.session_state.mensagem_venda = (
            "sucesso", "Venda finalizada!"
        )

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

def resumo_pagamento(pagamento, total_venda, recebido):
    st.subheader("Resumo do pagamento")
    st.write(f"Forma de pagamento: {pagamento}")
    st.write(f"Total da venda: R$ {total_venda:.2f}")

    if pagamento == "Dinheiro" and recebido is not None:
        st.divider()
        st.write(f"Recebido: R$ {recebido:.2f}")

        if recebido < total_venda:
            falta = total_venda - recebido
            st.warning(f"Faltam R$ {falta:.2f} para completar o pagamento.")
        else:
            troco = recebido - total_venda
            st.info(f"Troco: R$ {troco:.2f}")
            st.write(f"Entrada em dinheiro desta venda: R$ {total_venda:.2f}")
    else:
        st.caption("Este pagamento não acrescenta dinheiro físico ao caixa.")


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