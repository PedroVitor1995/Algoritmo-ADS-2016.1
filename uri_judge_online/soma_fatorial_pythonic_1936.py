import math

def main():

	n = int(input())

	qtd_fatores = 0

	for f in sorted([math.factorial(i) for i in range(1, 10)], reverse=True):
		qtd, n = divmod(n, f)
		qtd_fatores += qtd

	print(qtd_fatores)

if __name__ == '__main__':	
	main()