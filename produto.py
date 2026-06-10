"""Modelo e validacoes de produto. """


class Produto:
    """Representa um produto cadastrado no estoque."""

    def __init__(self, codigo, nome, categoria, preco, quantidade):
        self.codigo = self._validar_codigo(codigo) 
        self.nome = self._validar_texto(nome, "nome")
        self.categoria = self._validar_texto(categoria, "categoria")
        self.preco = self._validar_preco(preco)
        self.quantidade = self._validar_quantidade(quantidade)

    def atualizar(self, nome=None, categoria=None, preco=None, quantidade=None):
        """Atualiza campos editaveis do produto."""
        if nome is not None:
            self.nome = self._validar_texto(nome, "nome")
        if categoria is not None:
            self.categoria = self._validar_texto(categoria, "categoria")
        if preco is not None:
            self.preco = self._validar_preco(preco)
        if quantidade is not None:
            self.quantidade = self._validar_quantidade(quantidade)

    def registrar_saida(self, quantidade):
        """Reduz a quantidade em estoque, validando disponibilidade."""
        quantidade = self._validar_quantidade(quantidade)
        if quantidade == 0:
            raise ValueError("A quantidade vendida deve ser maior que zero.")
        if quantidade > self.quantidade:
            raise ValueError("Estoque insuficiente para essa venda.")
        self.quantidade -= quantidade

    def to_dict(self):
        """Converte o produto para dicionario, usado na persistencia JSON."""
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco": self.preco,
            "quantidade": self.quantidade,
        }
        

    @classmethod
    def from_dict(cls, dados):
        """Cria um produto a partir de um dicionario."""
        return cls(
            dados["codigo"],
            dados["nome"],
            dados["categoria"],
            dados["preco"],
            dados["quantidade"],
        )

    @staticmethod
    def _validar_codigo(codigo):
        codigo = int(codigo)
        if codigo <= 0:
            raise ValueError("O codigo deve ser um numero positivo.")
        return codigo

    @staticmethod
    def _validar_texto(valor, campo):
        valor = str(valor).strip()
        if not valor:
            raise ValueError(f"O campo {campo} nao pode ficar vazio.")
        return valor

    @staticmethod
    def _validar_preco(preco):
        preco = float(preco)
        if preco <= 0:
            raise ValueError("O preco deve ser positivo.")
        return preco

    @staticmethod
    def _validar_quantidade(quantidade):
        quantidade = int(quantidade)
        if quantidade < 0:
            raise ValueError("A quantidade nao pode ser negativa.")
        return quantidade

    def __str__(self):
        return (
            f"Codigo: {self.codigo} | Nome: {self.nome} | "
            f"Categoria: {self.categoria} | Preco: R$ {self.preco:.2f} | "
            f"Qtd: {self.quantidade}"
        )
