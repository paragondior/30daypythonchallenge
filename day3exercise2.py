#Exercise 3: Grading System
#Ask the user to enter their examination score.

#Use these grading conditions:
#Score	Grade
#80–100	A
#70–79	B
#60–69	C
#50–59	D
#Below 50	F


#Challenge: What happens if someone enters 150 or -10? Your program should reject invalid scores.

score = int(input("Enter your score"))
if score < 0 or score > 100:
    print("Invalid value, scores must not be more  than 100")
elif score < 50:
    print("F")
elif score < 60:
    print ("D") 
elif score < 70:
    print("C")
elif score < 80 :
    print ("B") 
else :
    print("A")      