
#VDivida = float(input('\nDigite o Valor da sua divida:'))
VDivida = 1000
NParcelas = 3
PJuros = 10
#Valor Inicial
print(f'Total: R$1000 Juros: R$0 Número de Parcelas:1 Valor da Parcela: R$1000')

for NParcelas in range(1,13,1):
    juros = VDivida * (PJuros/100)
    VTotalDivida = VDivida + juros
    VParcela = VTotalDivida / NParcelas
    if NParcelas in {3,6,9,12}:
        print(f'Total: R${VTotalDivida} Juros: R${juros} Número de Parcelas: {NParcelas} Valor da Parcela: R${VParcela}')
        PJuros = PJuros + 5
