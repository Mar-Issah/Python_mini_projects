from cryptography.fernet import Fernet
'''
# we don't need it again once it is created add ode to make it runs only once or check if file exist and it is not empty

def create_key():
  key = Fernet.generate_key()
  with open('key.key', 'wb') as file:
    file.write(key)'''

# create_key()

def get_key():
  with open('key.key', 'rb') as file:
    key = file.read()
    return key

# Just the key would have worked just making it stronger by adding file_password
file_password = input('What is your file password?: ')
key = get_key() + file_password.encode('utf-8')
fernet_key = Fernet(key)

# decrypt password. to remove the b''. then use decode()
def view():
  with open('passwords.txt', 'r') as file:
     for line in file.readlines():
       data = line.rstrip()
       user, password = data.split('-->>')
       print(f'User: {user}, Password: {fernet_key.decrypt(password.encode())}')


# encrypt password. make sure it is decoded so it is not store as bytes string i.e b'str'
def add():
  name = input('What is your account name?: ')
  password = input('What is your password?: ')

  with open('passwords.txt', 'a') as file:
    file.write(name + '-->>' + fernet_key.encrypt(password.encode()).decode() + '\n')


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
