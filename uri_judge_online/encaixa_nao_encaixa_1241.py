def main():

	n = int(input())

	for i in range(n):
		t1, t2 = input().split(' ')
		if len(t2) > len(t1):
			if t2[::-1] == t1[::-1][0:len(t2)]:
				print('encaixa')
		else:
			print('nao encaixa')

if __name__ == '__main__':
	main()