# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

# max_attempts=4
# attempts=0


# while attempts<max_attempts:
#     password=input("Input a password: ")
#     correct_password="admin@123"

#     if password==correct_password:
#         print("Access is granted")
#         break
    
#     attempts+=1
#     print(f"Invalid input.You only have {max_attempts-attempts} left")

#     if attempts==max_attempts:
#        print("The account has been blocked")



    #    OR

correct_password="admin@123"
attempts=4

for i in range(attempts):
    password=input("Input a password: ")
    if password==correct_password:
        print("Access is granted")
        break
    else:
        rem_attempt=attempts-(i+1)
        print(f"Wrong password. {rem_attempt} attempts left,try again!!")

        if rem_attempt==0:
            print("The account has been blocked")
        else:
            continue