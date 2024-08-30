# Question 1:  Write a program that displays a numbers 1 to 50 inside a list.

num1=list(range(1,51))
print(num1)
# ------------------------------------------------------------------------------------------------------------------
# Question 2: From 1 above display the ones divisible by 7 or 5 inside a list.
# num1=list(range(1,51))
# for z in num1:
#     if z%7==0 or z%5==0:
#         print(z)
    # OR
num1=[]
for z in range(1,51):
    if z%7==0 or z%5==0:
        num1.append(z)

print(num1)
# -------------------------------------------------------------------------------------------------------------------
# Question 3: Find sum and average of values in the range between 10 to 40.

sumation=0

for i in range(11,40):
    sumation += i
print("Sumation is: ",sumation)
average=sumation/len(range(11,40))
print("Average is: ",average)
# -----------------------------------------------------------------------------------------------------------------
# Question 4: Put in a list the first 10 odd numbers between 10 to 50. 

oddnum=[]
for m in range(10,51):
    if m%2!=0:
        oddnum.append(m)
        if len(oddnum)==10:
            break
        
print(oddnum)
# -----------------------------------------------------------------------------------------------------------------
# Question 5: write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.

multiply=int(input("Enter a number: "))
for x in range(1,11):
    print(f"{multiply} x {x} = {multiply*x}")
# --------------------------------------------------------------------------------------------------------------
# Question 6: write a program that counts and prints the number of even numbers between 1 and 50 using a for loop

even=[]
for i in range(2,50):
    if i%2==0:
        even.append(i)

print(even)
print("The number of even numbers between 1 and 50 is: ",len(even))

#    OR
even_count=0
for i in range(1,50):
    if i%2==0:
        even_count+=1 #OR even_count=even_count+1
print(even_count)

# ---------------------------------------------------------------------------------------------------------------
# Question 7: ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.

ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
total = 0

for name,quantity in ls1:
    # name=i[0]
    total += quantity #i[1]
   
print("The total quantity is: ",total)
    #  OR

# total = 0
# for name, number in ls1:
#     total += number

# print(total) 

#   OR

ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
total = 0

for i in ls1:
    # name=i[0]
    quantity=i[1]
    total += quantity #i[1]
   
print("The total quantity is: ",total)




