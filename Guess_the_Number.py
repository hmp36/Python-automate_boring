# This is a guess the number game. 

import random
print ('Hello. What is your name?')

name = input()
secretNumber = random.randint(1, 20)
print (''+ name +'?!' ' Cool!' ' That is a very fine name! ' + name+ ', I am thinking of a number between 1 and 20. What is it? ')


# Ask the player to guess 6 times

for guessesTaken in range (1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('too low.')
    elif guess > secretNumber:
        print ('too high.')
    else:
        break

# This condition is for the correct guess.

if guess == secretNumber:
    print('Nice, ' + name + '.' ' You nailed it!' ' You guessed in ' + str(guessesTaken) + ' guesses.')
else:
    print ('Nope. Sorry, man. The number was '+ str(secretNumber) + '. Better luck next time!')
