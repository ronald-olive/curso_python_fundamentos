contatos = {
    "amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"},
    "rose@gmail.com": {"nome": "Rose", "telefone": "3443-2121"},
    "katia@gmail.com": {"nome": "Katia", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}


for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)