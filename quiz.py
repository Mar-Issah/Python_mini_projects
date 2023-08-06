print('**********************************')
print('WELCOME TO A NEW ADVENTURE!!')
print('**********************************')

is_playing = input('Do you want to play this game?. Type yes/no: ')

if is_playing.lower() != 'yes':
  quit()

score = 0

print('\n--- OKay! Let\'s do this :-D---\n')

correct= 'Corrrect!'
wrong = 'WRONG! Please try again'

ans = input('What is the last month of the year?: ')
if ans.lower() == 'december':
  print(correct)
  score += 1
else:
  print(wrong)

ans = input('What does JS stand for?: ')
if ans.lower() == 'javaScript':
  print(correct)
  score += 1
else:
  print(wrong)

ans = input('What does OS stand for?: ')
if ans.lower() == 'operating system':
  print(correct)
  score += 1
else:
  print(wrong)

print(f'DONE! You got {str(score)} out of 3 correct')
