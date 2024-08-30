# INTEGERS-whole numbers(both positive and negative)
# to convert to float,use float()
y=99
print(type(y))
# it adds a decimal place
print(float(y))
print(type(float(y)))

# **used as exponential e.g 2^5
m=2
p=5
print(m**p)
# / (Division operator-gives the whole decimal) 
d = 2 
f = 5  
print(d / f)

# % (Modulo operator - This is the remainder of division)
a = 2 
c = 5  
print(a % c)

# // (Floor operator - Division that result into whole numbers)
b= 30 
q= 7   
print(b//q)


# FLOAT-decimal numbers
# to convert to int,use int()
x=29.7896
# int ignores the numbers in the deecimal places,so we use round instead
print(int(x))
# this converts to the nearest whole number
print(round(x))
# this converts to 2 decimal places as has been specified i.e round(value,decimals)
print(round(x,2))