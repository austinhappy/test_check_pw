password = 'a123456'
n = 3

while n > 0:
	pw = input('enter the password:')
	if pw == 'a123456':
		print('password is correct')
		break
	elif n == 1:
		print('no chance to login')
		break
	else:
		n = n - 1
		print('wrong password! %s chances remained' % n )