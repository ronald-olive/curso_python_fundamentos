contatos = {"amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('amanda@gmail.com', {'nome': 'Amanda', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError