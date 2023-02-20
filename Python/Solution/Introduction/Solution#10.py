# 10. En su casa le solicitan que realice un algoritmo en Python,
# que permita calcular el valor a pagar por concepto de
# energía eléctrica. Los datos que se conocen son los
# siguientes:
# - Mes de consumo - Valor kw 
# -Total kw consumido en el mes - estrato

estrato = int(input('\ningrese su estrato: '))
valor_kw = 100
total_wk_consumido = valor_kw * 30
mes_de_consumo = valor_kw * total_wk_consumido

if estrato == 1:
    valor_estrato = 90*mes_de_consumo / 100

elif estrato == 2:
    valor_estrato = 70*mes_de_consumo / 100

elif estrato == 3:
    valor_estrato = 40*mes_de_consumo / 100

elif estrato == 4:
    valor_estrato = 20*mes_de_consumo / 100

else:
    valor_estrato = 0
    
pagar = mes_de_consumo - valor_estrato

print(f'su total a pagar es de: {pagar}')
