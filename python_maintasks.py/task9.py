# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****

# Prompt the user for the number of rows
row=int(input("Enter a number of rows: "))

# Print the pattern of stars
for i in range(1, row + 1):

    print("*" * i)
