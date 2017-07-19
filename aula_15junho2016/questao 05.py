"""05. Leia um numero inteiro (3 digitos),
calcule e escreva a soma de seus elementos (C + D + U)."""

valor = input("Digite um numero inteiro de 3 digitos")
centena = valor / 100
dezena = (valor % 100) / 10
unidade = (valor % 10)
valor_total = centena + dezena + unidade
print "A soma dos tres digitos do valor %d eh %d" %(valor, valor_total)
