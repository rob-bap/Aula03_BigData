# # Estrutras 

# idade = int(input('Digite sua idade: '))

# # >, <, <=, >=, == (igualdade), != (diferente)
# if idade >= 18: 
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade')



# Classificação de pontos

pontos = int(input("Informe seus pontos: "))

if pontos >= 100:
    total = pontos + 10
    print(f'Excelente! Sua pontuação total foi {total}.')

elif pontos >= 50:
    total = pontos + 5
    print(f'Muito bom! Sua pontuação total foi {total}.')

elif pontos >= 30:
    total = pontos + 2
    print(f'Sua pontuação total foi {total}.')

else:
    print(f'Sua pontuação foi {pontos}.')

print('Fim')