password = input('What is your password?: ')

while True:
		mode = input('Do you want to add or view password? Type add/view: \n\nPress q to quit.\nEnter: ')

		if mode == 'q':
			break

		if mode.lower() == 'add':
			pass
		elif mode == 'view':
			pass
		else:
			print('Invalid')
			continue
