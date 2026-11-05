#Day 4 — Exercise 4: Your Challenge
#Write a program that prints numbers from 1 to 10 but skips number 5.

#Requirements:
#- Use a for loop.
#- Use continue.
#- Do not use multiple print statements.
for i in range(1,11):
    if i ==5:
        continue
    print(i)