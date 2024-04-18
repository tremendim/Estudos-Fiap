'A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários '
'a controlar suas fontes de receitas, gastos, dívidas e investimentos.'
'Ela precisa realizar uma votação para escolher qual dia da semana é o melhor '
'para a realização das lives com o time da mentoria financeira. Desenvolva um '
'programa em que os colaboradores informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) '
'da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.'
'Observação: Verifique o número de colaboradores que irão participar da votação para programar sua estrutura de repetição."'

print('Digite o Numero de Colaboradores')
NColaboradores = int(input())
cont = 0

for cont in range (NColaboradores):
    print('\nDigite a letra do dia da semana escolhido:')
    print('A - Segunda-Feira')
    print('B - Terça-Feira')
    print('C - Quarta-Feira')
    print('D - Quinta-Feira')
    print('E - Sexta-Feira')
    dia = input()
    if dia == 'A':
        print('Seu dia escolhido foi Segunda-Feira')
    elif dia =='B':
        print('Seu dia escolhido foi Terça-Feira')
    elif dia =='C':
        print('Seu dia escolhido foi Quarta-Feira')
    elif dia =='D':
        print('Seu dia escolhido foi Quinta-Feira')
    elif dia =='E':
        print('Seu dia escolhido foi Sexta-Feira')
    else:
        print('Letra não valida')