# ARITHMETIC OPERATOR
# addition(+)
# subtraction(-) 
# division(/)
# multiplication(*)
# floor operator(//)-returns the integer ignoring the remainder
print(20//3)
# modulo(%)-returns the remainder after division
print(20%3)
# power(**)
print(20**5)
print(20**2)


# ASSINGMENT OPERATORS
# These are operators used to shorten arithmetic operations operators.
# 	Example:	
# x=3
# 	x = x + 3 = 6 is same as x+=3     # the result is 6
#     x  = x * 3 = 9 is same as x*=3       # the result is 9

# =
a=10 
# +=
a=a+1 #10+1=11
a+=1 #11+1=12
print(a)
# -=
a=a-1 #12-1=11
a-=1 #11-1=10
print(a)
# *=
a=a*20 #10*20
a*=20 #20*20
print(a)
# /=
a=20 
a/=3
print("Division is: ",a)
# %=
a=20
a%=3
print("Modulo is: ",a)

# COMPARISON OPERATORS
# < (less than) Example: print(3<10)#True
print(3<10)
# > (greater than) Example: print(5>3)	 #True
print(5>3)
# == (Check equality-checks the value) Example: print(10==10)True
print(10==10)
# ===(TRIPLE EQUALITY-checks the data type and value)
# print(20==="20")-NOT IN PYTHON
# != (Check Inequality) Example: print(3!=4) True
print(3!=4)
# >= (Greater than or equal to): print(3 >= 3) #True
print(3 >= 3)
# <= (Less than or equal to): print(3 <= 2) #False
print(3 <= 2)


# LOGICAL OPERATORS-used to perform loical operations
# used to compare conditions


# logical AND(and)-returns true if ALL conditions are true
a=10<20 and 30<40 and 1>2
print(a)


# logical OR(or)-returns true if there's any condition that is true
a=10<20 or 30<40 or 1>2
print(a)
# A	      B 	A and B     A or B
# True	 True	True		True
# True	 False  False		True
# False	 True   False		True
# False	 False  False		False

# logical NOT(not)-returns true if the operand is false.used to invert the current boolean. This occurs when your intention is to get the opposite of some result.
a=True
print(a)

# IN - used to check if a string is in a data structure (list, tuple) 


# BITWISE OPERATORS
