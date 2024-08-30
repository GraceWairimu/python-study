# Tuple is a collection of data
# Enclosed with ()
# Immutable-cannot be edited so change it to list,edit then return to tuple
# Ordered-elements use index
# Creating a tuple
my_tuple=("lilian","kimani","grace")

# Converting a list into a tuple-use tuple()
x=[1,2,3,4,5]
print(x)
x=tuple(x)
print(x)

# Converting a tuple into a list-use list()
my_tuple=("lilian","kimani","grace",1000,2000)
# my_tuple[2]="manfred"-can't modify tuple so change to list
my_tuple=list(my_tuple)
my_tuple[2]="wairimu"
my_tuple=tuple(my_tuple)
print(my_tuple)


days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])
#2. Using a function a find the length of the tuple.
print(len(days))
#3. Replace Thursday with Thur
days=list(days)
days[3]="Thur"
days=tuple(days)
print(days)
#4. Add a Sat
days=list(days)
days.append("Sat")
days=tuple(days)
print(days)

# Membership-checking if an item is part of the list,tuple/set
print("lilian" in my_tuple)
print("wachira" in my_tuple)

# tuples are identified by , e.g
a= 1,
print(type(a))
