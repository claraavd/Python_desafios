import random

def jogar():

    print('*'*36)
    print('Bem vindo(a) ao jogo de adivinhação!')
    print('*'*36)
    
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    
    print("Níveis de dificuldade: (1)Fácil (2)Médio (3)Difícil")
    nivel = int(input("Defina o nível de dificuldade:"))
    
    if (nivel==1):
        total_de_tentativas = 20
    elif (nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5    
    
    rodada = 1
    
    for rodada in range (1,total_de_tentativas+1):
        print("Tentativa {} de {}:".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número que deve ser entre 1 e 100: ")
        chute = int(chute_str)
        
        if(chute < 1 or chute > 100):
            print("Você digitou um número inválido, por favor digite um número entre 1 e 100!")
            continue
    
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
    
        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    
        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()