# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .

# While true-always loops until it finds break

while True:
    num1=input("Enter the first number: ")
    num2=input("Enter the second number: ")

    if num1.isdigit() and num2.isdigit():
       num1=int(num1)
       num2=int(num2)
       sumation=num1+num2
       break
    elif num1.isdecimal() and num2.isdecimal():
       num1=float(num1)
       num2=float(num2)
       sumation=num1+num2
       break
    else:
       print("Invalid character entered")
       
print(sumation)