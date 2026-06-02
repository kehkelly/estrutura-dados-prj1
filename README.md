# Sistema de Estoque e Vendas

Repositorio sugerido para entrega:
<https://github.com/Rub3n1t0/estrutura-dados-prj1>

Projeto de linha de comando em Python para cadastrar produtos, controlar vendas,
consultar estoque e gerar relatorios simples.

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

- Cadastrar produto com codigo unico.
- Editar nome, categoria, preco e quantidade.
- Remover produto pelo codigo.
- Buscar produto por codigo com busca binaria.
- Buscar produtos por nome com busca linear.
- Registrar venda validando estoque disponivel.
- Listar produtos ordenados por codigo.
- Filtrar produtos por categoria.
- Mostrar relatorio de estoque baixo.
- Mostrar produto com menor e maior preco.
- Salvar e carregar dados em arquivo JSON.
- Registrar logs simples em `operacoes.log`.

## Estrutura

- `main.py`: menu e fluxo da aplicacao.
- `produto.py`: classe Produto e validacoes.
- `estoque.py`: cadastro, buscas, vendas e relatorios.
- `arquivos.py`: salvar, carregar e registrar logs.
- `dados_exemplo.json`: arquivo com produtos de exemplo.
- `RELATORIO.md`: explicacao curta sobre busca, ordenacao e Big-O.

## Exemplos de uso

Ao executar `python main.py`, escolha uma opcao:

```text
1. Cadastrar produto
4. Buscar produto por codigo
6. Registrar venda
7. Listar produtos ordenados por codigo
0. Sair
```

Exemplo de venda:

```text
Codigo do produto vendido: 101
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
