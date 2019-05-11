import random

def jogar():

    print('Bem vindo ao jogo de advinhacao!')

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    nivel = int(input('Qual o nivel? (1) facil (2) medio (3) dificil:'))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas))

        chute_str = input('Digite um numero entre 1 e 100: ')

        print('Voce digitou: ', chute_str)

        chute = int(chute_str)

        numero_invalido = chute < 1 or chute > 100

        if(numero_invalido):
            print('Digite um numero entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print('Voce acertou! Voce fez {} pontos'.format(pontos))
            break
        elif(maior):
            print('Voce errou. O chute foi maior que o numero secreto')
        elif(menor):
            print('Voce errou. O chute foi menor que o numero secreto')
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        
    print('Fim do jogo')

if(__name__== "__main__"):
    jogar()