import random
import operator
player = dict()
i = 1
value = 0
empate = True

print('-=-=-=-=-=-=-=-=-=-=-=-')
print('        SORTEIO        ')
print('-=-=-=-=-=-=-=-=-=-=-=-')
for c in range(0, 4):
    player['player'+str(c+1)] = random.randint(1, 6)

while empate:
    for k, v in player.items():
        r = random.randint(1, 6)
        if r not in player.values():
            player[k] = r
            empate = False
        else:
            r = random.randint(1, 6)
            empate = True

for k, v in player.items():
    print(f'  O {k} pegou {v}')
ordem = sorted(player.items(), key=operator.itemgetter(1), reverse=True)

print('-=-=-=-=-=-=-=-=-=-=-=-')
print('        RANKING        ')
print('-=-=-=-=-=-=-=-=-=-=-=-')
for c in range(0, len(ordem)):
    print(i, 'º lugar:', ordem[c][0], 'com ', ordem[c][1])
    i += 1