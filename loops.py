# A for loop is used to perform a repetitive task over and over. You can also loop through a list and get individual values as below:
# We first use range function to generate numbers. It's always best to typecast the range in a list or a tuple . Then we get individual values using a loop.

x= list(range(2,10))
for i in x:
  if i % 2 == 0:
     print(i)

x=[1,2,3,4,5,6]
for i in x:
    print(i)
    print(x)

# display a list of numbers between 0 and 1000
# range (10,1000)
y=list(range(10,1000))
for i in y:
    print(i)

# iterate through numbers between 20 and 100
z=list(range(20,101))
for i in z:
    print(i)

    # OR
even_numbers=[]
for i in range(20,100):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# break-stops the loop
for i in range(51):
    print(i)
    if i==40:
        break
