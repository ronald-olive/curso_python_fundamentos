contatos = {"amanda@gmail.com": {"nome": "Amanda", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["amanda@gmail.com"] = {"nome": "Ama"}

print(contatos["amanda@gmail.com"])  # {"nome": "Amanda", "telefone": "3333-2221"}

print(copia["amanda@gmail.com"])  # {"nome": "Ama"}