C = int(input())
for i in range(0, C):
	num = 0
	avg = 0
	tmp = 0
	test_input = input()
	list_a = test_input.split(' ')
	list_a = list(map(int, list_a))
	num = list_a[0]
	del list_a[0]
	avg = (sum(list_a))/num
	for i in list_a:
		if(i > avg):
			tmp = tmp+1
	per = (tmp/num)*100
	print('%.3f' %per + '%')