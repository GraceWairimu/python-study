# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
import datetime

# Get today's date
today = datetime.date.today()
# print(today.day) #current day
# print(today.month) #current month
# print(today.year) #current year

# Get user's date of birth
DOB=input("Enter your date of birth(yyyy/mm/dd): ")
x=DOB.split("/")
# print(x)

DOB_year=int(x[0])
DOB_month=int(x[1])
DOB_day=int(x[2])



years=today.year-DOB_year
months=today.month-DOB_month
days=today.day-DOB_day

if months<0:
    years-=1
    # months=12+months
    # OR
    months+=12

print(f"{years} years {months} month(s) {days} days")

# error on days,months and year



