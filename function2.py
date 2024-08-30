# parameters-
# arguments-

def hello(name):
    print(f"Hello,{name}!")

hello("Grace")
hello("Wairimu")
hello("Hez")
hello(21)

# 2--- Create afunction that calculates the area of a triangle using parameters and arguments
# def triangle_area():
#     base=20
#     height=10
#     area=(base*height)*0.5
#     print(area)
# triangle_area()

def triangle_area(base,height):
    area=(base*height)*0.5
    return area

b=int(input("Input the base: "))
h=int(input("Input the height: "))
triangle_area(b,h)


# 3--- Create a function that calculates the area of a rectangle and take the users input while using parameters and arguments

# def rectangle_area():
#     area=(base*height)
#     print(area)

# base=int(input("Enter the base: "))
# height=int(input("Enter the height: "))

# rectangle_area()

def rectangle_area(length,width):
    area=(length*width)
    # print(f"The area of the rectangle is {area}")-----we don't use print inside a function
    return area #anything after return is not recognised and won't run.

len=int(input("Enter the base: "))
width=int(input("Enter the height: "))
rectangle_area(len,width)
rectangle_area(50,15)
# when using return,incase I want to pri nt the output in the terminal,I can do as follows:
x=rectangle_area(len,width)
print(f"The area of the rectangle is {x}")


# Create a function that checks if a number is even.take the users input,use return 
def even_number(number):
    
    if number%2==0:
        check="Even number"
    else:
        check="Odd number"
    
    return check

num=int(input("Enter a number: "))
z=even_number(num)
print(f"The number is an {z}")


