'''Design a program that takes a birthday as input and prints 
the user’s age and the number of days, hours, minutes and seconds 
until their next birthday.'''

from datetime import *

#Get Today's Date
today = date.today()
print("Today: " +  today.strftime('%A %d, %b %Y'))

