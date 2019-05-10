print('Bem vindo ao jogo de advinhacao!')

numero_secreto = 42
total_tentativas = 3
rodada = 1

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
        print('Voce acertou!')
        break
    elif(maior):
        print('Voce errou. O chute foi maior que o numero secreto')
    elif(menor):
        print('Voce errou. O chute foi menor que o numero secreto')
    
print('Fim do jogo')