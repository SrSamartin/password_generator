# Gerador Automático de Senhas

import random
import string

# Função que define as variáveis, englobando 3 tipos diferentes de caracteres em uma única variável denominada "options" (Opções) e definindo a variável "password_user" como uma string em branco.
def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ""

# Loop que, dentro do escopo passado pelo usuário, define aleatóriamente cada caracter da senha.
    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit
    
    return password_user

choice_user = input("Quantos dígitos na senha? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida!")
    quit()

# Após as verificações, é retornada a senha completa ao usuário.
response = password_generator(len_pass = choice_user)
print(f'Senha gerada:\n{response}')
