contatos = {"amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"}}

resultado = contatos.pop("amanda@gmail.com")  # {'nome': 'Amanda', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("amanda@gmail.com", {})  # {}
print(resultado)