
print('Informe o tipo de rendimento que deseja fazer o saque:')
print(' 1 - CDB') 
print('2 - LCI')
print('3 - LCA)')
TRendimento = input()

if TRendimento == '1':
    VInvestido = float(input('Digite o valor investido'))
    DInvestidos = int(input('Digite a quantidade de dias que o valor permaneceu investido'))
    if DInvestidos <= 180:
        VAliquota = VInvestido*(22.5/100)
        VTotal = VInvestido - VAliquota
        print(f'Seu valor investido é R$:{VInvestido} e sua aliquota é de R${VAliquota} e seu valor com o desconto é de R${VTotal}')
    elif (181<DInvestidos<=360):
        VAliquota = VInvestido*(20/100)
        VTotal = VInvestido - VAliquota
        print(f'Seu valor investido é R$:{VInvestido} e sua aliquota é de R${VAliquota} e seu valor com o desconto é de R${VTotal}')
    elif (361<DInvestidos<=720):
        VAliquota = VInvestido*(17.5/100)
        VTotal = VInvestido - VAliquota
        print(f'Seu valor investido é R$:{VInvestido} e sua aliquota é de R${VAliquota} e seu valor com o desconto é de R${VTotal}')
    elif DInvestidos > 720:
        VAliquota = VInvestido*(15/100)
        VTotal = VInvestido - VAliquota
        print(f'Seu valor investido é R$:{VInvestido} e sua aliquota é de R${VAliquota} e seu valor com o desconto é de R${VTotal}')
elif TRendimento == '2' or '3':
    print('Seu valor investido está isento do IR!')
else:
    print('Valor invalido')

              
    