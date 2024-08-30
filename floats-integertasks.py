# Questions
# 1
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp1 = 56.8926
print(round(temp1))
# 2
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp2=56.8926
print(round(temp2,2))
# 3
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp3=56.8926
print(round(temp3,3))
# 4
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926
# NB: Use string  slice & concatenation, but have result as float 
temp4=56.8926
temp4=str(temp4)
wholenumber=temp4[3]
print(wholenumber)
decimalplaces=temp4[4:7]
print(decimalplaces)
temp4=wholenumber + "." + decimalplaces
print(temp4)
print(float(temp4))
print(type(float(temp4)))
# OR
temp4=56.8926
temp4=str(temp4)
temp4=temp4[3:7]
temp4=temp4[0] + "." + temp4[1:]
temp4=float(temp4)
print(temp4)


