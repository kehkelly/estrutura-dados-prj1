"""Interface de linha de comando do sistema de estoque e vendas."""

from arquivos import carregar_estoque, registrar_log, salvar_estoque
from produto import Produto


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Entrada vazia. Tente novamente.")


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Digite um numero inteiro valido.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", ".").strip())
        except ValueError:
            print("Digite um numero valido.")


def exibir_produtos(produtos, tamanho_pagina=5):
    if not produtos:
        print("Nenhum produto encontrado.")
        return

    for indice, produto in enumerate(produtos, start=1):
        print(produto)
        if indice % tamanho_pagina == 0 and indice < len(produtos):
            input("Pressione Enter para continuar...")


def cadastrar(estoque):
    try:
        codigo = ler_int("Codigo: ")
        nome = ler_texto("Nome: ")
        categoria = ler_texto("Categoria: ")
        preco = ler_float("Preco: R$ ")
        quantidade = ler_int("Quantidade: ")

        produto = Produto(codigo, nome, categoria, preco, quantidade)
        estoque.cadastrar_produto(produto)
        salvar_estoque(estoque)
        registrar_log(f"Produto cadastrado: codigo {codigo}")
        print("Produto cadastrado com sucesso.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def editar(estoque):
    codigo = ler_int("Codigo do produto para editar: ")
    produto = estoque.buscar_por_codigo(codigo)

    if produto is None:
        print("Produto nao encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    nome = input(f"Nome ({produto.nome}): ").strip() or None
    categoria = input(f"Categoria ({produto.categoria}): ").strip() or None
    preco_texto = input(f"Preco ({produto.preco:.2f}): ").replace(",", ".").strip()
    quantidade_texto = input(f"Quantidade ({produto.quantidade}): ").strip()

    try:
        preco = float(preco_texto) if preco_texto else None
        quantidade = int(quantidade_texto) if quantidade_texto else None
        estoque.editar_produto(codigo, nome, categoria, preco, quantidade)
        salvar_estoque(estoque)
        registrar_log(f"Produto editado: codigo {codigo}")
        print("Produto editado com sucesso.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def remover(estoque):
    codigo = ler_int("Codigo do produto para remover: ")
    try:
        estoque.remover_produto(codigo)
        salvar_estoque(estoque)
        registrar_log(f"Produto removido: codigo {codigo}")
        print("Produto removido com sucesso.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def buscar_codigo(estoque):
    codigo = ler_int("Codigo para buscar: ")
    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        print("Produto nao encontrado.")
    else:
        print(produto)


def buscar_nome(estoque):
    termo = ler_texto("Nome ou parte do nome: ")
    exibir_produtos(estoque.buscar_por_nome(termo))


def registrar_venda(estoque):
    codigo = ler_int("Codigo do produto vendido: ")
    quantidade = ler_int("Quantidade vendida: ")

    try:
        produto = estoque.registrar_venda(codigo, quantidade)
        salvar_estoque(estoque)
        registrar_log(
            f"Venda registrada: codigo {codigo}, quantidade {quantidade}"
        )
        print(f"Venda registrada. Estoque atual: {produto.quantidade}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def listar_categoria(estoque):
    categoria = ler_texto("Categoria: ")
    exibir_produtos(estoque.listar_por_categoria(categoria))


def relatorio_estoque_baixo(estoque):
    try:
        limite = ler_int("Limite de estoque baixo: ")
        exibir_produtos(estoque.relatorio_estoque_baixo(limite))
    except ValueError as erro:
        print(f"Erro: {erro}")


def relatorio_precos(estoque):
    menor = estoque.menor_preco()
    maior = estoque.maior_preco()

    if menor is None:
        print("Nenhum produto cadastrado.")
        return

    print("Produto com menor preco:")
    print(menor)
    print("\nProduto com maior preco:")
    print(maior)


def exibir_menu():
    print("\n==== Sistema de Estoque e Vendas ====")
    print("1. Cadastrar produto")
    print("2. Editar produto")
    print("3. Remover produto")
    print("4. Buscar produto por codigo")
    print("5. Buscar produtos por nome")
    print("6. Registrar venda")
    print("7. Listar produtos ordenados por codigo")
    print("8. Listar produtos por categoria")
    print("9. Relatorio de estoque baixo")
    print("10. Relatorio de menor e maior preco")
    print("0. Sair")


def main():
    estoque = carregar_estoque()

    opcoes = {
        "1": cadastrar,
        "2": editar,
        "3": remover,
        "4": buscar_codigo,
        "5": buscar_nome,
        "6": registrar_venda,
        "7": lambda estoque_atual: exibir_produtos(
            estoque_atual.listar_ordenados_por_codigo()
        ),
        "8": listar_categoria,
        "9": relatorio_estoque_baixo,
        "10": relatorio_precos,
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "0":
            salvar_estoque(estoque)
            print("Dados salvos. Ate mais!")
            break

        acao = opcoes.get(opcao)
        if acao is None:
            print("Opcao invalida.")
        else:
            acao(estoque)


if __name__ == "__main__":
    main()
