# Question1: Write a Python program that checks if a variable num is positive. If it is, further check if it is divisible by both 2 and 3. Print appropriate messages for each case.

# num=float(input("Enter a number: "))
# if num>0:
#     if num%2==0 and num%3==0:
#         result=f"{num} is positive and divisible by  both 2 and 3"
#     else:
#         result=f"{num} is positive but not divisible by both 2 and 3"
# else:
#     result=f"{num} is negative"

# print(result)

# Question2: Write a Python program that checks a username and password. If both are correct, print "Login successful". If either the username or password is incorrect, print "Login failed".

# username=input("Enter your username: ")
# password=input("Enter your password: ")
# correct_username="Grace"
# correct_password="1234"

# if username==correct_username and password==correct_password:
#     check="Login successful"
# else:
#     check="Login failed"

# print(check)


# Question3: Write a Python program that checks if a given string is a palindrome (reads the same forward and backward)

# original_word=input("Enter what you want to check if it is a palindrome: ")
# reverse_word=original_word[::-1]
# if original_word==reverse_word:
#     print(f"{original_word} is a palindrome")
# else:
#     print(f"{original_word} is not a palindrome")


# Question4: Write a Python program that calculates the Body Mass Index (BMI) and categorizes it into Underweight, Normal weight, Overweight, and Obesity based on standard BMI ranges.

# weight=float(input("Enter your weight in kg(kilograms): "))
# height=float(input("Enter your height in m(metres): "))
# bmi=weight/(height**2)
# if bmi>=30.0:
#     value="Obesity"
# elif bmi>=25.0:
#     value="Overweight"
# elif bmi>=18.5:
#     value="Healthy weight"
# else:
#     value="Underweight"

# print(value)

# Question5: Write a Python program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
# NB research on python loops

# for x in range(1,101):
     
#      if x%3==0:
#         print("Fizz")
#      elif x%5==0:
#         print("Buzz")
#      elif x%15==0:
#         print("FizzBuzz")
#      else:
#         print(x)

for num in range(1, 101):
  if num % 15 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)


