# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

def phonenumber():

    phone_number=input("Enter your phone number: ")

    if phone_number.startswith("+254") and len(phone_number)==13:
       new_number="+254" + phone_number[4:]
    elif phone_number.startswith("254") and len(phone_number)==12:
       new_number="+254" + phone_number[3:]
    elif phone_number.startswith("07") and len(phone_number)==10:
       new_number="+254" + phone_number[1:]
    elif phone_number.startswith("7") and len(phone_number)==9:
       new_number="+254" + phone_number
    elif phone_number.startswith("01") and len(phone_number)==10:
       new_number="+254" + phone_number[1:]
    elif phone_number.startswith("1") and len(phone_number)==9:
       new_number="+254" + phone_number
    else:
       new_number="Phone number is invalid"

    print(new_number)

phonenumber()

# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

def speed_function():
    speed=int(input("Enter the speed: "))
    speed_limit=70
    demerit_point=0

    if speed<=speed_limit:
      print("OK")

    elif speed>speed_limit and speed<=75:
      demerit_point+=1

    else:
      demerit_point=1
      demerit_point+=round((speed-75)/5)
    if demerit_point>12:
       print("License suspended")
    else:
        demerit_point=demerit_point

    print(f"The demerit point is {demerit_point}")

speed_function()


# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

def stock():
   prods = [["omo","30kshs","300"], ["milk","50kshs","200"],["bread","45kshs","359"], ["coffee","5kshs","79"]]
   total_stock=0

   for i in prods:
      quantity=int(i[2])
      total_stock+=quantity

   print(total_stock)

stock()


# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.

def largest():
   num1=int(input("Enter the first number: "))
   num2=int(input("Enter the second number: "))
   num3=int(input("Enter the third number: "))
   num4=int(input("Enter the fourth number: "))

   if num1>num2 and num1>num3 and num1>num4:
      print(f"{num1} is the largest")
   elif num2>num1 and num2>num3 and num2>num4:
      print(f"{num2} is the largest")
   elif num3>num1 and num3>num2 and num3>num4:
      print(f"{num3} is the largest")
   else:
      print(f"{num4} is the largest")

largest()


# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.

def check():
   correct_email="admin@mail.com"
   correct_password="Admin@123"
   tries=4

   for i in range(tries):
     email=input("Enter an email: ")
     password=input("Enter a password: ")
     if email==correct_email and password==correct_password:
            print("Login successful")
            break
     else:
          rem_tries=tries-(i+1)
          print(f"Invalid username or password.You only have {rem_tries} left")

          if rem_tries==0:
            print("The account has been blocked")
          else:
            continue

check()