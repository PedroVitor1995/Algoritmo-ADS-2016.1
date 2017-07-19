"""32. Leia um numero inteiro (3 digitos), calcule e escreva a diferenca entre o numero e seu inverso."""

numero = input ('Digite um numero inteiro (3 digitos): ')

numero1 = str(numero / 100)
numero2 = str((numero % 100) /10)
numero3 = str(numero % 10)

inverso_numero = str (numero3 + numero2 + numero1)
inverso_numero = int(inverso_numero)
diferenca = numero - inverso_numero

print ('A diferenca do numero %d e seu inverso %d e %d ') % (numero,inverso_numero,diferenca)