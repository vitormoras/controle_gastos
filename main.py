from function import cadastrar_categoria, cadastrar_transacao, saldo_total

cadastrar_receita = cadastrar_categoria("Receita")
cadastrar_contas = cadastrar_categoria("Contas")
cadastrar_viagens = cadastrar_categoria("Viagens")
cadastrar_lazer = cadastrar_categoria("Lazer")

cadastrar_transacao(
    descricao="Salario Jan/2025",
    valor= 3000,
    categoria=cadastrar_receita
    )

cadastrar_transacao(
    descricao="Salario Fev/2025",
    valor= 3000,
    categoria=cadastrar_receita
    )

cadastrar_transacao(
    descricao="Compra Marmita",
    valor= -22,
    categoria=cadastrar_contas
    )

total = saldo_total()

print(f"Seu saldo total é {total}")

