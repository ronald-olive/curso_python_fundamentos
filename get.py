contatos = {"amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "amanda@gmail.com", {}
)  # {"amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"}
print(resultado)