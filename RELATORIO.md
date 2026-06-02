# Relatorio curto

## Escolhas de estrutura

O sistema usa dois vetores para representar os produtos:

- `produtos_nao_ordenados`: guarda os produtos na ordem de cadastro.
- `produtos_ordenados_codigo`: guarda os mesmos produtos ordenados por codigo.

Essa escolha atende ao requisito de trabalhar com vetor nao ordenado e vetor
ordenado no mesmo projeto.

## Busca linear por nome

A busca por nome usa o vetor nao ordenado. Como os nomes nao estao em ordem
alfabetica, o sistema precisa percorrer todos os produtos comparando o termo
digitado com o nome de cada produto.

Complexidade:

- Melhor caso: O(1), se o produto procurado aparece logo no inicio.
- Pior caso: O(n), se o produto aparece no fim ou nao existe.
- Caso medio: O(n).

Essa busca foi escolhida porque permite encontrar partes do nome, por exemplo
buscar `mouse` e encontrar `Mouse sem fio`.

## Busca binaria por codigo

A busca por codigo usa o vetor ordenado por codigo. O sistema compara o codigo
procurado com o produto do meio do vetor. Se o codigo procurado for maior, a
busca continua na metade direita. Se for menor, continua na metade esquerda.
Esse processo se repete ate encontrar o produto ou concluir que ele nao existe.

Complexidade:

- Melhor caso: O(1), se o codigo esta exatamente no meio.
- Pior caso: O(log n).
- Caso medio: O(log n).

A busca binaria foi escolhida porque o codigo e unico e o vetor e mantido
ordenado a cada insercao e remocao.

## Insercao e remocao

Para inserir um produto, o sistema primeiro verifica se o codigo ja existe.
Depois encontra a posicao correta no vetor ordenado e insere o produto nessa
posicao. O vetor nao ordenado recebe o produto no final.

Complexidade da insercao no vetor ordenado:

- Encontrar posicao: O(log n).
- Inserir deslocando elementos: O(n).
- Resultado final: O(n).

Na remocao, o produto precisa ser removido dos dois vetores. Como listas em
Python precisam localizar e deslocar elementos, a remocao tem complexidade O(n).

## Validacoes

O sistema segue as regras de negocio:

- Nao permite codigo duplicado.
- Nao permite venda com estoque insuficiente.
- Preco precisa ser positivo.
- Quantidade nao pode ser negativa.
- Campos de texto nao podem ficar vazios.
