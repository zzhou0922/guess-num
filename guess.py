# Generate a random integer (1-100) without print it out.
# Let the user guesses the number repeatly
# Ouput "Bingo!" if the user guesses right.
# Let the user know if she/he guess larger or smaller compare to the correct number.

import random

result = random.randint(1, 100)
count = 0


while True:
	guess = input('Please enter a number: ')
	guess = int(guess)
	count += 1
	if guess == result:
		print('Bingo! You got it!')
		print('Here is your', count, 'attempt(s).')
		break
	elif guess < result:
		print('Your guess is smaller.')			
	else:
		print('Your guess is larger.')
	print('Here is your', count, 'attempt(s).')
	print()
			
