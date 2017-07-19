def quest20():
	numero_n = input("Numero N: ")
	soma = 0

	for i in range(1,numero_n + 1):
		if i % 2 != 0:
			soma += 1/float(i)
		else:
			soma -= 1/float(i)	

	print "Soma = %.2f" % soma

def main():
	quest20()

if __name__ == '__main__':
	main()