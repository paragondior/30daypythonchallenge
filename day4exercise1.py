#Exercise 2: Multiplication Table
#Ask the user to enter a number.

#Your program should print its multiplication table from 1 to 12
number = int(input("Enter a number"))
for i in  range(1,13):
   answer = number * i
   print(f"{number} x {i} = {answer}")