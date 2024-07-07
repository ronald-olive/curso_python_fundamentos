contato = {"nome": "Amanda", "telefone": "3333-2221"}

contato.setdefault("nome", "Rose")  # "Amanda"
print(contato)  # {'nome': 'Amanda', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Amanda', 'telefone': '3333-2221', 'idade': 28}