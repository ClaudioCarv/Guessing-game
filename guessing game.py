import os
import random
import time
import emoji
import platform
import colors

def limpar():
    if platform.system() == 'Windows':
        os.system('cls') 

def title():
    print('{}=:=:=:=:=:=:=:=:=:={}'.format(colors.cores['verde'], colors.cores['limpa']).center(80))
    print('{}{}Jogo da adivinhação{}'.format(colors.tipos['negrito'],colors.cores['verde'], colors.cores['limpa']).center(84))
    print('{}=:=:=:=:=:=:=:=:=:={}'.format(colors.cores['verde'], colors.cores['limpa']).center(80))

#limpar a tela assim q iniciar 
limpar() 

vt = 0 #vitorias
dr = 0 #derrotas

#loop do game
while True: 
    #randomização dos numeros
    num = random.randint(0, 5)
    title()
    jg = int(input('{}\nDigite 1 para jogar e 2 para sair: {}'.format(colors.cores['verde'], colors.cores['limpa'])))
    
    if (jg == 1):

        print('{}\nVamos começar{}'.format(colors.cores['verde'], colors.cores['limpa']))
        time.sleep(1)
        print('{}\nVou pensar em um numero entre 0 e 5 e você terá que adivinhar{}'.format(colors.cores['verde'], colors.cores['limpa']))
        time.sleep(3)
        print('{}Pensando...{}'.format(colors.cores['verde'], colors.cores['limpa']))
        time.sleep(4)
        print('{}{}PENSEI !{}'.format(colors.tipos['negrito'], colors.cores['verde'], colors.cores['limpa']))
        time.sleep(1)
        print(num)
    elif(jg == 2):
        print('{}Encerrado{}'.format(colors.cores['vermelho'], colors.cores['limpa']))
        break
    else:
        print('{}Digite de acordo com o que se pede{}'.format(colors.cores['amarelo'], colors.cores['limpa']))
        break

    #escolha do jogador
    esc = int(input('{}\nDigite aqui o numero que você acha que eu pensei: {}'.format(colors.cores['azul'], colors.cores['limpa']))) 
    print('{}Deixa eu ver...{}'.format(colors.cores['verde'], colors.cores['limpa']))
    time.sleep(1)

    #vitorias
    if(esc == num): 
        print('{}{}\nPARABÉNS, VOCÊ ACERTOU!!! ERA {}{}{}'.format(colors.tipos['sublinhado'],colors.cores['verde'], num, colors.cores['limpa'],emoji.emojize(':beaming_face_with_smiling_eyes: :beaming_face_with_smiling_eyes: :beaming_face_with_smiling_eyes:')))
        vt += 1

    #derrotas
    elif esc != num: 
        dr += 1
        print('{}{}\nHAHAHAHAHAHA VOCÊ ERROU, ERA {}{}{}'.format(colors.tipos['sublinhado'], colors.cores['vermelho'], num, colors.cores['limpa'],emoji.emojize('😂😂😂😂😂😂')))
    print('{}{}\nVitórias: {}{}'.format(colors.tipos['sublinhado'], colors.cores['verde'], colors.cores['limpa'], vt))
    print('{}{}Derrotas: {}{}'.format(colors.tipos['sublinhado'], colors.cores['verde'], colors.cores['limpa'], dr))

    #jogar novamente
    dnv = str(input('{}Deseja jogar novamente ? S/N: {}'.format(colors.cores['azul'], colors.cores['limpa']))).lower() 
    

    if(dnv == 's'):
        limpar()
    elif(dnv == 'n'):
        print('{}Encerrado{}'.format(colors.cores['vermelho'], colors.cores['limpa']))
        break
    else:
        print('{}você fez algo de errado, tente executar novamente.{}'.format(colors.cores['amarelo'], colors.cores['limpa']))
        break