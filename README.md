# Sistema de Estoque e Vendas

Repositório sugerido para entrega:
<https://github.com/Rub3n1t0/estrutura-dados-prj1>

Projeto de linha de comando em Python para cadastrar produtos, controlar vendas,
consultar estoque e gerar relatórios simples.

## Como executar

1. Tenha Python 3 instalado.
2. No terminal, entre na pasta do projeto.
3. Execute:

```bash
python main.py
```

O sistema salva os dados automaticamente em `dados.json`, que ja vem com alguns
produtos de exemplo. O arquivo `dados_exemplo.json` fica como copia separada dos
dados iniciais.

## Funcionalidades

- Cadastrar produto com codigo único.
- Editar nome, categoria, preço e quantidade.
- Remover produto pelo código.
- Buscar produto por código com busca binária.
- Buscar produtos por nome com busca linear.
- Registrar venda validando estoque disponível.
- Listar produtos ordenados por código.
- Filtrar produtos por categoria.
- Mostrar relatório de estoque baixo.
- Mostrar produto com menor e maior preço.
- Salvar e carregar dados em arquivo JSON.
- Registrar logs simples em `operacoes.log`.

## Estrutura

- `main.py`: menu e fluxo da aplicação.
- `produto.py`: classe Produto e validações.
- `estoque.py`: cadastro, buscas, vendas e relatórios.
- `arquivos.py`: salvar, carregar e registrar logs.
- `dados_exemplo.json`: arquivo com produtos de exemplo.
- `RELATORIO.md`: explicação curta sobre busca, ordenação e Big-O.

## Exemplos de uso

Ao executar `python main.py`, escolha uma opção:

```text
1. Cadastrar produto
4. Buscar produto por código
6. Registrar venda
7. Listar produtos ordenados por código
0. Sair
```

Exemplo de venda:

```text
Código do produto vendido: 101
Quantidade vendida: 2
Venda registrada. Estoque atual: 10
```

## Git e GitHub

Exemplo de comandos para versionar o projeto:

```bash
git init
git add .
git commit -m "Cria sistema de estoque e vendas"
git branch -M main
git remote add origin https://github.com/Rub3n1t0/estrutura-dados-prj1.git
git push -u origin main
```

Neste ambiente, o comando `git` nao estava disponivel no terminal, entao os
commits precisam ser feitos em uma maquina onde o Git esteja instalado.
