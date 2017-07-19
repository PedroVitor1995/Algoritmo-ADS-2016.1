def main():
	numeros = input().split(' ')
	carta1 = int(numeros[0])
	carta2 = int(numeros[1])
	if carta1 > carta2:
		print(carta1)
	elif carta1 < carta2:
		print(carta2)
	else:
		print(carta1)

if __name__ == '__main__':
	main()