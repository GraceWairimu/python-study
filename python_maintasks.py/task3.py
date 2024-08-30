# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

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