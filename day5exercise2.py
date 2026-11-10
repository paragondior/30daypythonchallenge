#Next: Day 5 practical project — Student Score Manager
 #We'll combine what you've learned about lists.
 #Your program should:
 #1. Create a list containing five student scores
 #2. Print all the scores. 
 #3. Add another score using append(). 
 #4. Remove one score using remove(). 
 #5. Sort the scores in ascending order.  
 #6. Display the number of scores using len().
 #7. Display the highest and lowest scores. 
 #Hint: Python lets you access the first and last elements using: 
 #scores[0]   # First elementscores[-1]  # Last element

#Remember to sort the list before finding the highest and lowest scores.

students = [40,50,60,70,80]
print(students)

students.append(90)
print(students)

students.remove(80)
students.sort()
print(students)

print(len(students))

print(students[0])
print(students[-1])