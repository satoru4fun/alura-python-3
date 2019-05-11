def jogar():

    print('Bem vindo ao jogo de advinhacao!')

    palavra_secreta = 'banana'.upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    print(letras_acertadas)
    
    enforcou = False
    ganhou   = False
    erros = 0

    while(not enforcou and not ganhou):
        print('jogando...')
        chute = input('Qual a letra?')
        chute = chute.strip().upper()

        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute.upper()==letra.upper()):
                    letras_acertadas[index] = chute.lower()
                index += 1
        else:
            erros += 1
        
        enforcou = erros >= 6

        ganhou = '_' not in letras_acertadas

        print(letras_acertadas)
    
    if(ganhou):
        print('Voce ganhou!')
    else:
        print('Voce perdeu!')

    print('Fim do jogo')

if (__name__ == "__main__"):
    jogar()