def jogar():

    print('*'*36)
    print('Bem vindo(a) ao jogo da Forca!')
    print('*'*36)
    
    palavra_secreta = 'banana'
    
    enforcou = False
    acertou = False
    
    #Enquanto (True)
        while (not enforcou and not acertou):
    
        chute = input('Digite uma letra:')
        chute = chute.strip()
    
        index = 0
        for letra in palavra_secreta:
            if chute.upper == letra.upper:
                print('Encontrei a letra {} na posução {}!'.format (letra, index))
            index = index + 1
        print ('jogando..')
    
print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()