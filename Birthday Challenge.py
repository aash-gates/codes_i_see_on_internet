'''Design a program that takes a birthday as input and prints 
the user’s age and the number of days, hours, minutes and seconds 
until their next birthday.'''

from datetime import *

#Get Today's Date
today = date.today()
print("Today: " +  today.strftime('%A %d, %b %Y'))

dob_str = input("What is your Date of Birth? dd/mm/yyyy \n\n")
#Convert user input into a date
dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
dob = date(dobYear,dobMonth,dobDay)

#Calculate number of days lived
numberOfDays = (today - dob).days 

#Convert this into whole years to display the age
age = numberOfDays // 365
print("You are " + str(age) + " years old.")

#Retrieve the day of the week (Monday to Sunday) corresponding to the DoB.
