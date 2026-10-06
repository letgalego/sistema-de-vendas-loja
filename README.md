# 🛒 Sistema de Caixa de Loja

Projeto de estudo em Python com interface web em **Streamlit** para registrar vendas e saídas e acompanhar as movimentações de uma loja.

O sistema começou como um programa de terminal e passou a utilizar uma interface com menu lateral, formulários, tabelas e resumo de pagamento. A versão atual permite montar um carrinho com vários produtos antes de finalizar a venda.

## Funcionalidades

- Adicionar produtos ao carrinho com nome, quantidade e valor unitário.
- Calcular o total de cada item e o total da compra.
- Limpar os campos do produto após adicioná-lo com sucesso.
- Escolher a forma de pagamento: dinheiro, Pix ou cartão.
- Informar o valor recebido e calcular o troco nas vendas em dinheiro.
- Impedir a finalização de uma compra vazia ou com dinheiro insuficiente.
- Finalizar uma única venda com todos os itens do carrinho.
- Limpar o carrinho e os campos de pagamento após finalizar com sucesso.
- Registrar saídas com descrição e valor.
- Consultar as vendas e os produtos de cada compra em seções expansíveis.
- Consultar as saídas em uma tabela.
- Exibir o total de vendas, o total de saídas e o saldo das movimentações.
- Mostrar mensagens de sucesso e de validação na interface.

## Tecnologias

- **Python:** lógica do programa, validações e manipulação de listas e dicionários.
- **Streamlit:** campos de entrada, botões, menu lateral, colunas, containers, métricas e tabelas.
- **Session State:** mantém o carrinho, as vendas e as saídas entre as interações de uma mesma sessão.

## Estrutura dos arquivos

| Arquivo | Responsabilidade |
| --- | --- |
| `app.py` | Inicia a interface, organiza as telas, mostra o carrinho, os relatórios e os totais. |
| `formularios.py` | Monta os campos de entrada, cria os itens e as vendas, processa os callbacks dos botões e exibe o resumo de pagamento. |
| `validacoes.py` | Contém as funções de validação utilizadas pelo projeto, como `nome_validado()` e `valor_validado()`. |

O módulo deve se chamar `formularios.py`, no plural, para corresponder ao import utilizado em `app.py`. Os três arquivos devem estar na mesma pasta.

## Como executar

### Pré-requisitos

- Python instalado. Para executar os trechos atuais com aspas duplas dentro das f-strings, utilize **Python 3.12 ou superior**. Em versões anteriores, ajuste as aspas dessas expressões.
- Os arquivos `app.py`, `formularios.py` e `validacoes.py` na pasta do projeto.
- Streamlit instalado no ambiente usado para executar o programa.

### 1. Abra o terminal na pasta do projeto

No VS Code, abra a pasta do projeto e utilize o terminal integrado.

### 2. Crie um ambiente virtual — opcional

```bash
python -m venv .venv
```

Para ativar no Windows pelo Prompt de Comando:

```bat
.venv\Scripts\activate.bat
```

Para ativar no Windows pelo PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Para ativar no Linux ou macOS:

```bash
source .venv/bin/activate
```

### 3. Instale o Streamlit

```bash
python -m pip install -r streamlit
```

### 4. Inicie o sistema

```bash
python -m streamlit run app.py
```

Abra no navegador o endereço local exibido no terminal. Para encerrar o servidor, pressione `Ctrl+C` no terminal.

## Como utilizar

### Registrar uma venda

1. Escolha **Registrar venda** no menu lateral.
2. Preencha o produto, a quantidade e o valor unitário.
3. Clique em **Adicionar item**. O produto entra no carrinho e os campos do item são limpos.
4. Repita o processo para os outros produtos da mesma compra.
5. Escolha a forma de pagamento.
6. Se o pagamento for em dinheiro, informe o valor recebido e confira o troco.
7. Clique em **Finalizar venda**.

O botão de finalização fica desativado quando o carrinho está vazio. Se o pagamento for insuficiente, os itens permanecem no carrinho para permitir a correção. Somente compras finalizadas entram no total de vendas.

### Registrar uma saída

1. Escolha **Registrar saída** no menu lateral.
2. Preencha a descrição e o valor.
3. Clique em **Registrar saída**.

### Consultar o relatório

Escolha **Relatorio do dia** no menu lateral. As compras finalizadas aparecem em seções expansíveis, com os produtos e os dados de pagamento. Abaixo, uma tabela mostra as saídas registradas.

## Organização dos dados

### Item do carrinho

Cada item é um dicionário criado por `criar_item()`:

```python
{
    "produto": "Caderno",
    "quantidade": 2,
    "valor_unitario": 25.0,
    "valor_total": 50.0
}
```

### Venda finalizada

`criar_venda()` recebe os itens do carrinho e os dados de pagamento:

```python
{
    "itens": [
        {
            "produto": "Caderno",
            "quantidade": 2,
            "valor_unitario": 25.0,
            "valor_total": 50.0
        }
    ],
    "valor_total": 50.0,
    "forma_pagamento": "Dinheiro",
    "recebido": 100.0,
    "troco": 50.0
}
```

Nas vendas por Pix ou cartão, `recebido` e `troco` são `None`, pois esses campos não se aplicam. Os itens são copiados para a venda finalizada antes de limpar o carrinho.

### Saída

```python
{
    "descricao": "Compra de material de limpeza",
    "valor": 20.0
}
```

## Funções principais

| Função | Responsabilidade |
| --- | --- |
| `formulario_venda()` | Exibe os campos para adicionar um item ao carrinho. |
| `criar_item()` | Valida o produto, a quantidade e o preço e retorna um item. |
| `adicionar_e_limpar()` | Adiciona o item válido ao carrinho e limpa seus campos. |
| `formulario_pagamento()` | Exibe a forma de pagamento e o valor recebido, quando necessário. |
| `criar_venda()` | Valida o carrinho e o pagamento e retorna a compra completa. |
| `registrar_e_limpar()` | Finaliza a venda e limpa o carrinho e os campos. |
| `resumo_pagamento()` | Exibe o total, o recebido e o troco. |
| `formulario_saida()` | Exibe os campos de registro de saída. |
| `criar_saida()` | Valida a descrição e o valor e retorna uma saída. |
| `montar_tabela_vendas()` | Prepara os itens do carrinho ou de uma compra para exibição. |
| `montar_tabela_saida()` | Prepara as saídas para exibição. |

Os callbacks são passados aos botões **sem parênteses**, como `on_click=adicionar_e_limpar`. Assim, o Streamlit os executa ao clicar, antes de montar novamente os campos.

## Cálculos

| Resultado | Cálculo |
| --- | --- |
| Total do item | Quantidade × valor unitário |
| Total da compra | Soma dos totais dos itens do carrinho |
| Troco | Valor recebido − total da compra |
| Entrada em dinheiro de uma venda | Valor recebido − troco |
| Saldo das movimentações | Total de vendas − total de saídas |

Em uma compra totalmente paga em dinheiro, a entrada líquida em dinheiro é igual ao total da compra. Pix e cartão aumentam o total vendido, mas não acrescentam dinheiro físico ao caixa.

**A métrica atual “Caixa do dia” soma todas as formas de pagamento e desconta todas as saídas. Ela representa o saldo das movimentações, e não apenas o dinheiro físico disponível.** Ainda não há controle de saldo inicial ou da forma de pagamento das saídas.

## Limitações atuais

- Os registros ficam apenas em `st.session_state`: ainda não são gravados em arquivo ou banco de dados.
- Recarregar a página pode reiniciar a sessão e apagar os registros temporários. Encerrar o servidor também não preserva os dados.
- Cada sessão possui seus próprios dados; ainda não existe um caixa compartilhado entre vários usuários.
- Apesar do nome **Relatorio do dia**, o relatório mostra os registros da sessão, sem filtragem por data.
- Ainda não há remoção ou edição de itens do carrinho nem cancelamento de vendas finalizadas.
- Os valores monetários utilizam `float`; o projeto ainda não utiliza centavos inteiros ou `Decimal` para tratar precisão financeira.
- O sistema é um projeto de estudo e não emite documentos fiscais.

## Próximas melhorias

- Salvar e carregar os dados usando JSON ou SQLite.
- Registrar data e filtrar os relatórios por período (mês/ano).
- Remover ou editar itens do carrinho e cancelar a compra em andamento.
- Separar os totais de dinheiro, Pix e cartão nas métricas.
- Informar o saldo inicial e controlar saídas por forma de pagamento.
- Implementar abertura e fechamento do caixa.
- Exportar relatórios.
