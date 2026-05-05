valor_compra = float(input('Qual valor da compra?: '))

if valor_compra > 250.00:
    desconto = valor_compra * 0.16
    valor_total = valor_compra - desconto
    print(f'O valor total da compra com o desconto de 16% é de {valor_total}')

else:
    print(f'O valor da compra deu {valor_compra}')