def  main():

	respostas = []
	
	primeiro_texto = raw_input()
	
	while primeiro_texto:
		segundo_texto = raw_input()

		menor_texto, maior_texto = (primeiro_texto, segundo_texto) if len(primeiro_texto)<= len(segundo_texto) else (segundo_texto, primeiro_texto)

		tamanho_maior_substring = 0

		for i in range(len(menor_texto)):
			for j in range(i+1, len(menor_texto)+1):
				#print i, j, menor_texto[i:j]
				if menor_texto[i:j] in maior_texto \
					and len((menor_texto[i:j])) > tamanho_maior_substring:
					tamanho_maior_substring = len(menor_texto[i:j])
					
		respostas.append(tamanho_maior_substring)

		# Trata o erro de EOF
		try:
			primeiro_texto = raw_input()
		except:
			primeiro_texto = ''


	#escreve resposta
	for i in respostas:
		print i


if __name__ == '__main__':
	main()