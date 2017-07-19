"""4. Leia o valor do dolar e um valor em dolar,
calcule e escreva o equivalente em real (R$)."""

cotacao = input("Digite a cotacao: ")
valor_dolar = input("Digite o valor em dolar: ")
valor_reais = cotacao * valor_dolar
print "O valor %.2f dolares com cotacao a %.2f equivale a %.2f reais" %(valor_dolar, cotacao, valor_reais)
