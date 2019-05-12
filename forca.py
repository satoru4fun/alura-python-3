import random

def jogar():

    imprime_mensagem_boas_vindas()
    palavra_secreta = gera_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)
    
    enforcou = False
    ganhou   = False
    erros = 0

    while(not enforcou and not ganhou):
        chute = pede_chute()
        
        if(chute in palavra_secreta):
            confere_chute(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros >= 7

        ganhou = '_' not in letras_acertadas

        print(letras_acertadas)
    
    if(ganhou):
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta)

    print('Fim do jogo')

def imprime_mensagem_boas_vindas():
    print('Bem vindo ao jogo de forca!')

def gera_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    aleatorio = random.randrange(0,len(palavras))
    palavra_secreta = palavras[aleatorio].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Qual a letra?')
    chute = chute.strip().upper()
    return chute

def confere_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute.upper()==letra.upper()):
            letras_acertadas[index] = chute.lower()
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
    jogar()