# 1.Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.

a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
c=int(input("Enter a number c: "))
if a>b and a>c:
#     # print("The largest of the numbers is: ",a)
#     # or
    print(f"{a} is the largest of the numbers") #FORMATTED STRING-used to pass variables inside strings.
elif b>a and b>c:
    print("The largest of the numbers is: ",b)
else:
    print("The largest of the numbers is: ",c)

# EXAMPLE OF FORMATTED STRINGS
number=20
x=30
y=number + x
z= f"{number} + {x} = {y}"
print(z)



# 2.Take as input from a user the temperature if the temperature is above 30°C display
#  “The temperature is too high”,if the temperature is above 15 display “Normal temperature” 
# otherwise display “Cold temperature”

temperature=int(input("Input the temperature: "))
if temperature>30:
    print("The temperature is too high")
elif temperature>15:
    print("Normal temperature")
else:
    print("Cold temperature")

    # OR
# if temperature>30:
#     value=("The temperature is too high")
# elif temperature>15:
#     value=("Normal temperature")
# else:
#     value=("Cold temperature")   

# print(value) 

    #  OR-incase you are to start with temperature>15
# if temperature>15 and temperature<=30:
#     value=("Normal temperature")
# elif temperature<=15:
#     value=("Cold temperature")
# else:
#     value=("The temperature is too high")   

# print(value)



# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", 
# otherwise print "Conditions not met"

x=int(input("Enter x: "))
y=int(input("Enter y: "))
if x>=10 and x<=20 and y>100:
    print("Conditions met")
else:
    print("Conditions not met")



# 4. Write a Python program that checks if a variable password is equal to the string "secret123". 
# If it is, print "Access   granted", otherwise print "Access denied"

password=input("Key-in your password: ")
# if password=="secret123":
#     print("Access granted")
# else:
#     print("Access denied")

    # OR
correct_password="secret123"
if password==correct_password:
    print("Access granted")
else:
    print("Access denied")

    

# 5. Write a Python program that checks if a variable student_score is greater than 90.
#  If true, check if the attendance is greater than 80. If both conditions are true,
#  print "Excellent student", otherwise print "Good score, but attendance needs improvement"

student_score=int(input("Enter the student's score: "))
attendance=int(input("Enter the student's attendance: "))

if student_score>90:
    if attendance>80:
      print("Excelent student")
    else:
      print("Good score,but attendance needs improvement")


