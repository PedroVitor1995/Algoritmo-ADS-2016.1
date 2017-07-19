def main():
	palavra = 'Instituto Federal'

	for i in range(len(palavra)-1, -1, -1):
		print i, palavra[i]

if __name__ == '__main__':
	main()