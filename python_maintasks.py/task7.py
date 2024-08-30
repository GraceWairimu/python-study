# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
marks=int(input("Enter the student marks: "))

for i in range(101):
    if marks>79:
        value="A"
    elif marks >=60:
        value="B"
    elif marks >=50:
        value="C"
    elif marks>=40:
        value="D"
    else:
        value="E"

print(value)