import forca
import advinhacao


def escolher_jogo():
    jogo = int(input('Qual jogo quer jogar? (1) forca (2) advinhacao'))

    if(jogo == 1):
        print('Jogando forca...')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando advinhacao...')
        advinhacao.jogar()

if (__name__ == "__main__"):
    escolher_jogo()