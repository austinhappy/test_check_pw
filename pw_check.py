password = 'a123456'
n = 3

while n > 0:
	pw = input('enter the password:')
	n = n - 1
	if pw == password:
		print('password is correct')
		break
	else:
		print('wrong password!')
		if n > 0:	
			print(' %s chances remained' % n )
		else:
			print('no chances remained')
