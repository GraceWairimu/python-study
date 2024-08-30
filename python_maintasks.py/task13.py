# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# tries=0
# max_tries=3

# while tries<max_tries:
#       email=input("Enter an email: ")
#       password=input("Enter a password: ")
#       correct_email="admin@mail.com"
#       correct_password="Admin@123"

#       if email==correct_email and password==correct_password:
#             print("Login successful")
#             break
#       tries+=1
#       print(f"Invalid username or password.You only have {max_tries-tries} left")

#       if tries==max_tries:
#         print("The account has been blocked")

      #   OR
      # Using for loop

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
     
            
   


