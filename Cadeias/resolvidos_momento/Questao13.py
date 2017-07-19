#__*__  encoding:utf8 __*__
"""13. As normas para a exibição da bibliografia de um artigo cientifico, de uma monografia, de um livro,
texto etc., exigem que o nome do autor seja escrito no formato último sobrenome, sequência das
primeiras letras do nome e dos demais sobrenomes, seguidas de ponto final. Por exemplo, Antonio
Carlos Jobim seria referido por Jobim, A. C.. Escreva um programa que receba um nome completo e o
escreva no formato de bibliografia."""
import string
def main():	
	nome_completo = raw_input('Digite um nome completo: ')
	nome_completo = string.capwords(nome_completo)
	letras_minusculas = string.lowercase
	letras_maiucusculas = string.uppercase
	nome_completo = nome_completo.split()
	ultimo_sobrenome = ''
	resto_nome = ''
	for i in range(len(nome_completo)-1,-1,-1):
		ultimo_sobrenome = nome_completo[-1]
	for i in range(len(nome_completo)-1):
		resto_nome += (nome_completo[i] + ' ') 
	for letra in letras_minusculas:
		resto_nome = resto_nome.replace(letra,'')
	for letra in letras_maiucusculas:
		resto_nome = resto_nome.replace(letra,letra + '. ')
	formato = ultimo_sobrenome+", "+ resto_nome
	print formato
if __name__ == '__main__':
	main()