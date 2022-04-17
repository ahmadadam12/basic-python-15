"""
Create a program that asks 
the user to enter their name and their age. 
Print out a message addressed to them that 
tells them the year that they will turn 100 years old. 
"""

from datetime import date
name = input("enter your name: ")
age = int(input("enter your age: "))

todays_date = date.today()
year = int(todays_date.year)
#print(todays_date.year)

a = (year) + ((100 + age))

print(f"{name}, you'll be 100 y.o in {a}")

"""
 below is how to obtain date:
     # importing date class from datetime module
from datetime import date
  
# creating the date object of today's date
todays_date = date.today()
  
# printing todays date
print("Current date: ", todays_date)
  
# fetching the current year, month and day of today
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)
"""