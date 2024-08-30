# Collection of unique data-not repeated
# Unordered-cannot access values using index
# Enclosed with {}
# Mutable-can be altered

# Creating sets
my_set={1,2,3,4,5,6,7,8}
print(my_set)
# Converting tuple/lists to a set
x=[1,2,3,4,5]
x=set(x)
print(x)

my_tuple=("lilian","kimani","grace",1000,2000)
my_tuple=set(my_tuple)
print(my_tuple)

# Adding elements into a set
my_set.add(8)
print(my_set)

# Removing elemnts in a set
my_set.remove(4)
print(my_set)

# Membership-checking if an item is part of the list,tuple/set
print(6 in my_set)
print(9 in my_set)

# Union-used to combine all elements from different sets
x={"a","b","c","d"}
y={"e","f"}
z=x.union(y)
print(z)

# Intersection-returns elements common in both sets
a={1,2,3,4}
b={3,4,5,6}
c=a.intersection(b)
print(c)

# Difference-returns those elements in the first set and not in the second set
a={1,2,3,4}
b={3,4,5,6}
d={9,6,7,8}
c=a.difference(b).difference(d)
f=b.difference(a).difference(d)
print(c)
print(f)

# Symmetric Difference-returns elements in either set but not in both sets
a={1,2,3,4,}
b={3,4,5,6}
c=a.symmetric_difference(b)
print(c)


# QUESTION
days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

# Remove friday and sunday from the set using methods.
days.remove("friday")
print(days)
days.remove("sunday")
print(days)
# Add them back to the set
days.add("friday")
days.add("sunday")
print(days)
