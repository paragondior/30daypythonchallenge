#Final Day 4 Challenge — Number Guessing Game
#Let's combine what you've learned into a small project.

#Write a program that:
#1. Stores a secret number, for example 7.
#2. Asks the user to guess the number.
#3. Uses a while loop to keep asking until they guess correctly.
#4. If the guess is wrong, print Wrong guess. Try again!
#5. If correct, print Congratulations! You guessed correctly.

secret = 8
take = int(input("Enter the secret number"))
while take != secret:
    print("Wrong guess. Try again! ")
    take = int(input("Please guess again"))
  
if take == secret :
 print("Congratulations! You have guessed correctly.")

   