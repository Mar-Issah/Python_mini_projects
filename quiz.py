print('**********************************')
print('WELCOME TO A NEW ADVENTURE!!')
print('**********************************')

is_playing = input('Do you want to play this game?. Type yes/no: ')

if is_playing != 'yes':
  quit()

print('\n--- OKay! Let\'s do this :-D---\n')

correct= 'Corrrect!'
wrong = 'WRONG! Please try again'

ans = input('What is the last month of the year?: ')
if ans == 'December':
  print(correct)
else:
  print(wrong)

ans = input('What does JS stand for?: ')
if ans == 'December':
  print(correct)
else:
  print(wrong)

ans = input('What does OS stand for?: ')
if ans == 'December':
  print(correct)
else:
  print(wrong)
