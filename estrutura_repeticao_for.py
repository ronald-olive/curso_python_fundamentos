# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"
# exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adicione uma quebra de linha

# Exemplo utilizando a função buit-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
    