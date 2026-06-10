"""Operacoes de estoque usando vetores ordenado e nao ordenado."""

from produto import Produto


class Estoque:
    """Controla produtos e vendas. 

    produtos_nao_ordenados preserva a ordem de cadastro e permite busca linear
    por nome. produtos_ordenados_codigo fica sempre ordenado para busca binaria.
    """

    def __init__(self):
        self.produtos_nao_ordenados = []
        self.produtos_ordenados_codigo = []

    def cadastrar_produto(self, produto):
        if self.buscar_por_codigo(produto.codigo) is not None:
            raise ValueError("Codigo existente.")

        posicao = self._posicao_insercao(produto.codigo)
        self.produtos_ordenados_codigo.insert(posicao, produto)
        self.produtos_nao_ordenados.append(produto)

    def editar_produto(self, codigo, nome=None, categoria=None, preco=None, quantidade=None):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise ValueError("Produto nao encontrado.")
        produto.atualizar(nome, categoria, preco, quantidade)
        return produto

    def remover_produto(self, codigo):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise ValueError("Produto nao encontrado.")

        self.produtos_ordenados_codigo.remove(produto)
        self.produtos_nao_ordenados.remove(produto)
        return produto

    def buscar_por_codigo(self, codigo):
        """Busca binaria em vetor ordenado por codigo. Complexidade O(log n)."""
        codigo = int(codigo)
        inicio = 0
        fim = len(self.produtos_ordenados_codigo) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            produto = self.produtos_ordenados_codigo[meio]

            if produto.codigo == codigo:
                return produto
            if produto.codigo < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1

        return None

    def buscar_por_nome(self, termo):
        """Busca linear em vetor nao ordenado. Complexidade O(n)."""
        termo = termo.strip().lower()
        encontrados = []

        for produto in self.produtos_nao_ordenados:
            if termo in produto.nome.lower():
                encontrados.append(produto)

        return encontrados

    def registrar_venda(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise ValueError("Produto nao encontrado.")
        produto.registrar_saida(quantidade)
        return produto

    def listar_ordenados_por_codigo(self):
        return list(self.produtos_ordenados_codigo)

    def listar_por_categoria(self, categoria):
        categoria = categoria.strip().lower()
        return [
            produto
            for produto in self.produtos_nao_ordenados
            if produto.categoria.lower() == categoria
        ]

    def relatorio_estoque_baixo(self, limite):
        limite = int(limite)
        if limite < 0:
            raise ValueError("O limite nao pode ser negativo.")
        return [
            produto
            for produto in self.produtos_nao_ordenados
            if produto.quantidade < limite
        ]

    def menor_preco(self):
        if not self.produtos_nao_ordenados:
            return None
        return min(self.produtos_nao_ordenados, key=lambda produto: produto.preco)

    def maior_preco(self):
        if not self.produtos_nao_ordenados:
            return None
        return max(self.produtos_nao_ordenados, key=lambda produto: produto.preco)

    def carregar_produtos(self, produtos):
        self.produtos_nao_ordenados = []
        self.produtos_ordenados_codigo = []

        for produto in produtos:
            self.cadastrar_produto(produto)

    def to_list(self):
        return [produto.to_dict() for produto in self.produtos_nao_ordenados]

    def _posicao_insercao(self, codigo):
        inicio = 0
        fim = len(self.produtos_ordenados_codigo)

        while inicio < fim:
            meio = (inicio + fim) // 2
            if self.produtos_ordenados_codigo[meio].codigo < codigo:
                inicio = meio + 1
            else:
                fim = meio

        return inicio


def criar_estoque_com_dados(dados):
    estoque = Estoque()
    produtos = [Produto.from_dict(item) for item in dados]
    estoque.carregar_produtos(produtos)
    return estoque
