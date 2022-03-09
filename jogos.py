import jogodaforca
import jogodeadivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) para jogar Forca (2) para jogar Adivinhação")

jogo = int(input("Qual jogo você gostaria de jogar hoje? "))

if (jogo == 1):
    print("Jogando forca")
    jogodaforca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    jogodeadivinhacao.jogar()