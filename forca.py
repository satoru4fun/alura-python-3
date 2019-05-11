def jogar():

    print('Bem vindo ao jogo de advinhacao!')

    palavra_secreta = 'banana'
    
    enforcou = False
    ganhou   = False

    while(not enforcou and not ganhou):
        print('jogando...')
        chute = input('Qual a letra?')
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if(chute.upper()==letra.upper()):
                print('A letra {} foi encontrado em {}'.format(chute, index))
            index = index + 1

    print('Fim do jogo')

if (__name__ == "__main__"):
    jogar()