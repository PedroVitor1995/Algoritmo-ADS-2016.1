def main():

	qtd = int(input())

	for i in range(qtd):
		original = raw_input().upper()
		time1 = raw_input().upper()
		time2 = raw_input().upper()
		pts_t1 = 0
		pts_t2 = 0
		time = 0
		achou_primeiro_erro = False

		for j in range(len(original)):
			if time1[j] == original[j]:
				pts_t1 += 1
				if not achou_primeiro_erro and time2[j] != original[j]:
					time = 1
					achou_primeiro_erro = True

			if time2[j] == original[j]:
				pts_t2 += 1
				if not achou_primeiro_erro and time1[j] != original[j]:
					time = 2
					achou_primeiro_erro = True
			

		print("Instancia %d" % (i+1))

		if pts_t1 > pts_t2:
			print('time 1')
		elif pts_t1 < pts_t2:
			print('time 2')
		else:
			if achou_primeiro_erro:
				print('time %d' % time)
			else:
				print('empate')
		print('')

if __name__ == '__main__':
	main()