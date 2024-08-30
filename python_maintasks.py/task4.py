# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
email=input("Input the email: ")

if email.count("@")!=0 and email.count(".")!=0:
    print(f"{email} is valid")
else:
    print(f"{email} is not valid")