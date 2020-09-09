# Armstrong Number

start = 1042000
end = 702648265

for num in range(start,end + 1):
	qwerty = 0
	temp = num
	order = len(str(start))
	while temp > 0:
		data = temp % 10
		qwerty += data ** order
		temp //= 10
	if (num == qwerty):
		print("The first Armstrong Number is :", num)
		break