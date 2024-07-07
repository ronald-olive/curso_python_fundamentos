contatos = {
    "amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"},
    "rose@gmail.com": {"nome": "Rose", "telefone": "3443-2121"},
    "katia@gmail.com": {"nome": "Katia", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["amanda@gmail.com"]["telefone"]
del contatos["katia@gmail.com"]

# {'amanda@gmail.com': {'nome': 'Amanda'}, 'rose@gmail.com': {'nome': 'Rose', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)