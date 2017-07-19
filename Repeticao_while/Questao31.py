"""31. Escreva um algoritmo que leia um numero decimal (ate 3 digitos) e escreva o seu equivalente em
numeracao romana. Utilize funcoes para obter cada digito do numero decimal e para a transformacao
de numeracao decimal para romana (Dica: 1 = I, 5 = V, 10 = X, 50 = L, 100 = C, 500 = D, 1.000 = M)."""
def main():

	while True:
		numero_decimal = input('Digite um numero decimal de (3 digitos) ou 0 para sair: ')

		centena_romana = 0
		dezena_romana = 0
		unidade_romana = 0

		if numero_decimal <= 0:
			break
		else:
			centena_decimal = (numero_decimal / 100) * 100
			dezena_decimal = ((numero_decimal % 100) / 10) * 10
			unidade_decimal = numero_decimal % 10

			if centena_decimal >= 100 or centena_decimal <= 900:
				if centena_decimal == 100:
					centena_romana = 'C'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal == 200:
					centena_romana = 'CC'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal == 300:
					centena_romana = 'CCC'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal == 400:
					centena_romana = 'CD'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal == 500:
					centena_romana = 'D'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal == 600:
					centena_romana = 'DC'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal  == 700:
					centena_romana = 'DCC'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal == 800:
					centena_romana = 'DCCC'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'
				elif centena_decimal == 900:
					centena_romana = 'CM'
					if dezena_decimal >= 10 or dezena_decimal <= 90:
						if dezena_decimal == 10:
							dezena_romana = 'X'
						elif dezena_decimal == 20:
							dezena_romana = 'XX'
						elif dezena_decimal == 30:
							dezena_romana = 'XXX'
						elif dezena_decimal == 40:
							dezena_romana = 'XL'
						elif dezena_decimal == 50:
							dezena_romana = 'L'
						elif dezena_decimal == 60:
							dezena_romana = 'LX'
						elif dezena_decimal == 70:
							dezena_romana = 'LXX'
						elif dezena_decimal == 80:
							dezena_romana = 'LXXX'
						elif dezena_decimal == 90:
							dezena_romana = 'XC'

		numero_romano = centena_romana + dezena_romana

		print numero_romano





if __name__ == '__main__':
	main()