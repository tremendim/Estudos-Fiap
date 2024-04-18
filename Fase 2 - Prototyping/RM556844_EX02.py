

print('\nDigite o valor do Carro')
VCarro = float(input())
VAvista = VCarro - (VCarro*0.2)
parcelas = 6
Acrescimo = 3

print('O valor a vista com desconto é igual a R$:',VAvista)

while parcelas != 66:
    PAcrescimo = VCarro * (Acrescimo/100)
    VParcelado = VCarro + PAcrescimo
    Vparcelas = VParcelado/parcelas
    print(f'O preço final parcelado em {parcelas} é de R$ {VParcelado:.2f} com parcelas de R$ {Vparcelas:.2f}')
    parcelas = parcelas+6
    Acrescimo = Acrescimo + 3
