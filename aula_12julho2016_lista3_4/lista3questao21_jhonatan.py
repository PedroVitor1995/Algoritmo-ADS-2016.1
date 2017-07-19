def main():
	n_1 = 1
	n_2 = 1
	total = 0
	for i in range(50):
		print('%d/%d' % (n_1, n_2))
		total = total + (n_1/n_2)
		n_1 += 2
		n_2 += 1

	print('Total : %.2f.' % total)

if __name__ == '__main__':
	main()