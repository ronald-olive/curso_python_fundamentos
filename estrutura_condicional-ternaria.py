saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")