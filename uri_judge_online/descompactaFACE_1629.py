def main():

	while True:
		
		n = int(input())

		if n == 0: break

		for i in range(n):
			soma = sum([int(i) for i in list(input())])

			if soma > 20:
				soma = sum([int(i) for i in list(str(soma))])

		print(soma)


if __name__ == '__main__':
	main()