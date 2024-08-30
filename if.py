#NB:The indentation space only has to be same in a specific block. A block is specified using a full colon.
# IF ELSE STATEMENTS

x=10
if x>20:
    print("x is greater")
else:
    print("x is less than")

# take a users input of a number
# check if the number is even
# else display odd number
number=int(input("Enter a number: "))

if number%2==0:
    print("Is even")
else:
    print("Is odd")

# take a users input of a number
# check if the number is odd
# else display even number
number1=int(input("Enter a number: "))

if number1%2!=0:
    print("Is odd")
else:
    print("Is even")

# take a users input of a number
# check if the number is odd and greater than 50
# else display even number

number1=int(input("Enter a number: "))

if number1%2!=0 and number1>50:
    print("Is odd and greater than 50")
else:
    print("Is even or less than 50 ")

# Write a Python program that checks if a variable x is between 10 and 20(inclusive) and if
# another variable y is greater than 100.If both conditions are true,print "Conditions met"
# otherwise print "Conditions not met"

x=int(input("Enter x: "))
y=int(input("Enter y: "))
if x>=10 and x<=20:
    if y>100:
        print("Conditions met")
    else:
        print("Conditions not met")
else:
    print("Conditions not met")

#IF ELIF STATEMENTS
# GRADING SYSTEM-taking marks and grading
marks=int(input("Enter the marks: "))


if marks>=80:
      print("Grade is A")
elif marks>=70:
      print("Grade is B")
elif marks>=60:
      print("Grade is C")
elif marks>=50:
      print("Grade is D")
else:
      print("Grade is E")


# NESTED IF STATEMENTS
# Check if marks is between 0 and 100
# Otherwise display invalid marks

marks=int(input("Enter the marks: "))

if marks>=0 and marks<=100:
    if marks>=80:
      print("Grade is A")
    elif marks>=70:
      print("Grade is B")
    elif marks>=60:
      print("Grade is C")
    elif marks>=50:
      print("Grade is D")
    else:
      print("Grade is E")
else:
   print("Invalid marks")


#   QUESTION
# Write a program that checks if a number num is positive,negative,or zero.If the number is positive,
# it should further check if it is even or odd

num=int(input("Please enter a number: "))

if num<0:
    print("num is negative")
elif num==0:
    print("num is zero")
elif num>0:
    if num%2==0:
        print("num is positive and even")
    else:
        print("num is positive and odd") 
