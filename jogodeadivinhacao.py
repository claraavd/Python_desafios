print('*'*40)
print('Bem vindo(a) ao jogo de adivinhação!')
print('*'*40)
numero_secreto=45
chute=int(input('Digite um número:'))
if(chute==numero_secreto):
        print('Parabéns, você acertou!')
else:
        print('Que pena, tente outra vez!')