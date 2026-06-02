"""Funcoes de persistencia em JSON e logs simples."""

import json
from datetime import datetime
from pathlib import Path

from estoque import criar_estoque_com_dados


ARQUIVO_DADOS = Path("dados.json")
ARQUIVO_LOG = Path("operacoes.log")


def carregar_estoque(caminho=ARQUIVO_DADOS):
    caminho = Path(caminho)
    if not caminho.exists():
        return criar_estoque_com_dados([])

    with caminho.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return criar_estoque_com_dados(dados)


def salvar_estoque(estoque, caminho=ARQUIVO_DADOS):
    caminho = Path(caminho)
    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(estoque.to_list(), arquivo, ensure_ascii=False, indent=4)


def registrar_log(mensagem, caminho=ARQUIVO_LOG):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    caminho = Path(caminho)
    with caminho.open("a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{agora}] {mensagem}\n")
