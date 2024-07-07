contatos = {
    "amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"},
    "rose@gmail.com": {"nome": "Rose", "telefone": "3443-2121"},
    "katia@gmail.com": {"nome": "Katia", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "amanda@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["amanda@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["rose@gmail.com"]  # True
print(resultado)