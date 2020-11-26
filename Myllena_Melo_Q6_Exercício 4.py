player = dict()
quantgols = list()
partidas = 0
player['nome'] = str(input('Insira o nome do jogador(a): '))
quantpartidas = int(input('Quantas partidas ' + player['nome'] + ' participou: '))
for p in range(0, quantpartidas):
    quantgols.append(int(input('Quantos gols foram feitos na partida ' + str(p+1) + ' ? ')))

player['gols'] = quantgols
player['total'] = sum(quantgols)

print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print(player)
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 20)
print('O jogador(a) ', player['nome'], 'jogou ', len(quantgols), ' partidas.')
for p in range(0, quantpartidas):
    print('\t=> Na partida ', str(p+1), ' fez ', quantgols[p], ' gols.')
print('Foi um total de ', player['total'], 'gols.')