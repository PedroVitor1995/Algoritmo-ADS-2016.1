def divisores(a):
	for i in range(a, 0,-1):
		if a % i == 0:
			print "%d eh divisor" % (i)

def main():
	x = input("digite um numero: ")
	if x == 0:
		print("fim")
	else:
		divisores(x)
		main()

if __name__ == '__main__':
	main()		
