import random
quantjogos = int(input("Olá jogador(a), insira a quantidade de jogos que quer jogar: "))
i = 0
print('---------------------------------')
print('|            PALPITES           |')
print('---------------------------------')
for j in range(0, quantjogos):
    i += 1
    lista = random.sample (range(1, 60),6)
    print('Jogo', i, ':', (lista))