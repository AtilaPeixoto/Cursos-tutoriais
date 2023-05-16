teste = list()
teste.append('atila')
teste.append('31')
galera = []                 # a chamada de atenção é para que se escreva list como no exemplo da lista teste
galera.append(teste[:])     # lembre-se dos pontos dentro. sem eles as listas sao gemeas seamesas
print('tes[:] antes do maria', galera)
teste[0] = 'maria'           # é importante atribuir posiçao.
teste[1] = 20
print(teste)                # o interessante é que maria substituis o primeiro nome na lista porem como a atribuiçao foi feita posteriaor a copia os dois nomes foram lançados
#galera.append(teste)       # atila fica na galera sem este e maria esta em teste
print('posterior ao maria', galera)
###############################
galera = [['joao', 19], ['maria', 30], ['joaquim', 24], ['maria', 45]]
print(' nome de um idade do outro ', galera[0][0], galera[2][1])
for p in galera:
    print(p)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
for i in range(0, 3):
    teste.append(str(input('Nome ').strip().upper()))
    teste.append(int(input('Idade ')))
    galera.append(teste[:])            # por teste estar com maria vai apresentar erro/bug na primeira fusao
    teste.clear()                        # este limpa o teste e apartir do segundo ciclo nao existe mais erro/bug
print('esta é test apos o clear', teste)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade ')
    else:
        print(f'{p[0]} é menor de idade ')
print(galera)
