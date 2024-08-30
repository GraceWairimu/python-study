# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

def calculate_totalmarks(maths,eng,swa,sci,sos):
    total_marks=maths+eng+swa+sci+sos

    return total_marks

maths=int(input("Enter the maths score: "))
eng=int(input("Enter the eng score: "))
swa=int(input("Enter the swa score: "))
sci=int(input("Enter the sci score: "))
sos=int(input("Enter the sos score: "))

x=calculate_totalmarks(maths,eng,swa,sci,sos)
print("The total mark is: ",x)

def calculate_average(totalmarks):
    average=totalmarks/5

    return average

z=calculate_average(x)
print("The average is: ",z)

def get_grade(average):
    if average>=0 and average<=100:
       if average>79:
          value="A"
       elif average>=60:
          value="B"
       elif average>=50:
          value="C"
       elif average>=40:
          value="D"
       else:
          value="E"

    return value

q=get_grade(z)
print("The student's grade is: ",q)