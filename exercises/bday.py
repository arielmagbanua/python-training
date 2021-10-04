from datetime import *

firstname = input ("input your first name: ")
lastname = input ("input your last name: ")

bday_str = input("what is your date of birth? enter as dd/mm/yyyy: ")
bday_data = bday_str.split("/")
bdayDay = int(bday_data[0])
bdayMonth = int(bday_data[1])
bdayYear = int(bday_data[2])
bday = date(bdayYear, bdayMonth, bdayDay)
today = date.today()

print("Today is: " + today.strftime('%A %d, %b %Y'))
numberOfDayslived = (today-bday).days

print("Dear " + firstname.capitalize())
