aluno_lista = list()
aluno_listaC = list()
quantaluno = 0
i = 0
media = 0
aluno = -1
quantaluno = int(input('Insira a quantidade de alunos(a): '))

for j in range(0, quantaluno):
    aluno_lista.append(str(input('Insira o nome do aluno(a): ')))
    aluno_lista.append(float(input('Insira a 1ª nota: ')))
    aluno_lista.append(float(input('Insira a 2ª nota: ')))
    media = (float(aluno_lista[i+1])+float(aluno_lista[i+2]))/2
    aluno_lista.append(float(media))
    aluno_listaC.append(aluno_lista[i:])
    i += 4

i = 0
print("Nº\tNome\t\tMédia")
print('#################################')
for a in range(0, len(aluno_listaC)):
    print("%s\t%s\t\t%.2f" %
          (str(a), aluno_listaC[a][i], aluno_listaC[a][3]))
print('#################################')

while aluno != 77:
    if aluno != -1:
        print('Notas de: ', aluno_listaC[aluno]
              [i], ' são:', aluno_listaC[aluno][1:3])
        print('#################################')
    aluno = int(input('Insira o número do aluno(a) que deseja ver a nota. *77 encerra a tentativa* '))
print ('Você encerrou.')