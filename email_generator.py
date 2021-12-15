#!/bin/python3

import random
import os
import time
import sys

def email_senha():

    os.system('clear')

    print('''Gerador de email e senha\n''')

    # caracteres = '1, 2, 3, 4, 5, 6, 7, 8, 9, 0'
    caracteres = '_', '-', ''

    caracteres_random= random.choice(caracteres)
    final = random.randint(1, 100)

    print('Provedores de email disponiveis: Gmail, Protonmail, Hotmail\n')

    email_create = str(input('Digite qual provedor de email você quer (LEMBRE-SE: Digitar tudo em minusculo): '))

    if email_create == 'gmail':
        print('')
        time.sleep(1)

    elif email_create == 'protonmail':
        print('')
        time.sleep(1)

    elif email_create == 'hotmail':
        print('')
        time.sleep(1)
    else:
        print('\nProvedor indisponivel no momento...')
        time.sleep(4)
        email_senha()

    nome = str(input('\nDigite um nome para o seu email: '))
    sobrenome = str(input('\nDigite o seu sobrenome para complementar no email: '))

    try:
        # Montando a senha
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '#@$%&*-=+/_'

        # VARS_ALL
        vars_all = lower + upper + numbers + symbols

        # Tamanho da senha
        length = int(input('\nDigite o tamanho da sua senha (Limite de senha: 73)): '))

        if length > 73:
            print('\nSenha muito grande tente uma menor...')
            time.sleep(2)
            email_senha()

        # Gerando a senha
        password = ''.join(random.sample(vars_all , length))
        os.system('clear')
        print(f'Email: {nome}{caracteres_random}{sobrenome}{final}@{email_create}.com'.lower())
        print(f'\nsenha: {password}\n')
        sys.exit(0)

    except KeyboardInterrupt:
        os.system('clear')
        sys.exit(0)

email_senha()
