#Given:
#students = ["John", "Peter", "Sarah", "Michael", "David"]

#Write code to:
#. Remove "Sarah" using remove().
#2 Print the updated list.
students = ["John" , "Peter", "Sarah", "Michael", "David"]

students.remove("Sarah")
print(students)
#Given:
 #colours = ["Red", "Blue", "Green", "Yellow", "Black"]

#1. Use pop() to remove "Green" by its index.
  #2. Use another pop() to remove the last element 
  #3. Print the updated list.

colours = ["Red", "Blue", "Green", "Yellow", "Black"]
colours.pop(2)
colours.pop(-1)
print(colours)

#Given:
 #games = ["FIFA", "GTA", "Minecraft", "Call of Duty", "God of War"]

#1. Use del to remove "Minecraft".
 #2. Print the updated list.


games = ["FIFA","GTA", "Minecraft", "Call of Duty", "God of War"]
del games[2]
print(games)






