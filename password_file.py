file_password = input('What is your file password?: ')

def view():
  pass

def add():
  name = input('What is your account name?: ')
  password = input('What is your password?: ')

while True:
		mode = input('Do you want to add or view password? Type add/view: \n\nPress q to quit.\nEnter: ')

		if mode == 'q':
			break

		if mode.lower() == 'add':
			add()
		elif mode == 'view':
			view()
		else:
			print('Invalid')
			continue
