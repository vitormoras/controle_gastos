from categoria import Categoria
from transicao import Transacao

list_cat = []
lits_trans = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)

    list_cat.append(nova_categoria)

    return nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(
        descricao= descricao,
        valor= valor,
        categoria= categoria
    )
    
    lits_trans.append(nova_transacao)

    return nova_transacao

def saldo_total():
    total = 0

    for t in lits_trans:
        total = total + t.valor
    
    return total