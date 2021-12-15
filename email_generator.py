#!/bin/python3

import random
import os
import time

# Dados aleatorios

def email_senha():

    os.system('clear')

    print('''Gerador de email e senha\n''')

    # caracteres = '1, 2, 3, 4, 5, 6, 7, 8, 9, 0'
    caracteres = '_', '-', ''

    caracteres_random= random.choice(caracteres)
    final = random.randint(1,100)

    nome = str(input('Digite um nome para o seu email: '))
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
        print (f'\nEmail: {nome}{caracteres_random}{sobrenome}{final}@gmail.com')
        print(f'\nSenha: {password}')

    except KeyboardInterrupt:
        os.system('clear')
        exit()

email_senha()
