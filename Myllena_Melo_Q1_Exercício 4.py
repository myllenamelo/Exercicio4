#Usando essa tabela do campeonato pernambucano. • Criei uma tupla preenchida com esses times na ordem de 
# colocação depois: • Mostre os 3 primeiros colocados • Os últimos 4 colocados da tabela
#• Uma lista com os times em ordem alfabética. • Em que posição na tabela está o time de Vitória.

time = ("Sport Recife", "Náutico", "Santa Cruz", "Salgueiro","Central","Afogados","Vitória","Petrolina","América","Flamengo Arc")
print(time)
print('Os três primeiros colocados foram: ',time[0:3])
print('Os quatro últimos colocados foram: ',time[-4:])
print('Em ordem alfabética:',sorted(time))
print ('A posição de Vitória é: ',len('Vitória'),'º')

