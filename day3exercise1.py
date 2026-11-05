#Exercise 2: Age Eligibility Checker
#Ask the user for their age.
# If age is below 13, print You are a child.
# If age is between 13 and 19, print You are a teenager.
# Otherwise, print You are an adult.

age = int(input("Enter your age"))

if age < 13 :
    print("You are a child")

elif 13<= age <=19:
    print("You are a teenager")  

else:
    print("You are an adult")
