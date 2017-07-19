"""33. Leia um numero inteiro (3 digitos), calcule e escreva a soma do numero com seu inverso.
(Ex.: numero = 532 ; inverso = 235 ; soma = 532 + 235 = 767)."""

numero = input ('Digite um numero inteiro (3 digitos): ')

numero1 = str(numero / 100)
numero2 = str((numero % 100) /10)
numero3 = str(numero % 10)

inverso_numero = str (numero3 + numero2 + numero1)
inverso_numero = int(inverso_numero)
soma = numero + inverso_numero

print ('A soma do numero %d e seu inverso %d e %d ') % (numero,inverso_numero,soma)