#__*__  encoding:utf8 __*__
"""3. Leia uma letra e verifique se a letra digitada é vogal ou consoante."""
def main():
	letra = raw_input('Digite uma letra: ')
	if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
		print('A letra digitada eh vogal')
	else:
		print('A letra digitada eh consoante')

if __name__ == '__main__':
	main()