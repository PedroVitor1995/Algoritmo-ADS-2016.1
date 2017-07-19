"""26. Cada espectador de um cinema respondeu a um questionario no qual constava sua idade e a sua opiniao
em relacao ao filme (1=otimo, 2=bom, 3=regular, 4=pessimo). Escreva um algoritmo que leia a idade e
a opiniao das pessoas, calcule e mostre ao final: (FLAG: idade = -1).
a media das idades das pessoas que responderam otimo;
a quantidade de pessoas que respondeu regular;
o percentual de pessoas que respondeu bom entre os entrevistados"""
def main():
	soma_idades_pessoas_otimo = 0
	quantidade_pessoas_regular = 0
	media_idade_pessoas_otimo = 0
	percentual_pessoas_bom = 0
	cont_otimo = 0
	cont_regular = 0
	cont_bom = 0
	cont_total = 0


	while True:
		idade = input('\nDigite a idade de uma pessoa sendo -1 para sair: ')

		if idade == -1:
			break
		elif idade > 0:
			opiniao = input('\nDigite a opiniao do espectador sendo 1 - otimo, 2 - bom, 3 - regular, 4 - pessimo: ')
			cont_total = cont_total + 1
			if opiniao == 1:
				soma_idades_pessoas_otimo += idade
				cont_otimo += 1
			elif opiniao == 3:
				cont_regular += 1
			elif opiniao == 2:
				cont_bom += 1
	if cont_otimo > 0 and cont_total > 0:
		media_idade_pessoas_otimo = soma_idades_pessoas_otimo / cont_otimo
		percentual_pessoas_bom = (cont_bom * 100) / cont_total

	print('\nA media das idades das pessoas que responderam otimo foi %.2f anos') % media_idade_pessoas_otimo
	print('\nA quantidade de pessoas que responderam regular foi %d pessoas ') % cont_regular
	print('\nO percentual das pessoas qu e responderam bom ente os entrevistados foi %.2f %% ') % percentual_pessoas_bom
if __name__ == '__main__':
	main()