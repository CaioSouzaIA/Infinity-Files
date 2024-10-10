numero_secreto = 9
tentativas = 0

while tentativas < 3:
    palpite = int(input('Digite um número: '))
    tentativas += 1

    if palpite == numero_secreto:
        print('Parabéns, você acertou o número secreto!')
        break
    else:
        print('Errado, tente mais uma vez.')

else:
    print(f'Infelizmente, você esgotou o número de tentativas... o número secreto era: {numero_secreto}')
