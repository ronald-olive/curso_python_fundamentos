contatos = {"amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"}}

contatos.update({"amanda@gmail.com": {"nome": "Ama"}})
print(contatos)  # {'amanda@gmail.com': {'nome': 'Ama'}}

contatos.update({"rose@gmail.com": {"nome": "Rose", "telefone": "3322-8181"}})
# {'amanda@gmail.com': {'nome': 'Ama'}, 'rose@gmail.com': {'nome': 'Rose', 'telefone': '3322-8181'}}
print(contatos)