fname= "Grace"
print(fname)
# type() tells us the data type of the input
print(type(fname))
lname="Njuguna"

# concatenating the two variables into one
fullname=fname + " " + lname
print(fullname)
# Indexing(From the right we start with -1 but from the left we start with 0 )
print(fname[0])
# getting the e in Grace can be gotten two ways
print(fname[-1])
print(fname[4])

# Slicing is extracting a substring(while doing this,stick to the positive)
print(fullname[6:11])

# str function is used to convert a number to numeric string
age=25
age=str(age)
print(type(age))

x="30"
y="20"
z=x+y
print(z)

me="I am a student at TechCamp"
# displaying the word student
print(me[7:14])
print(me[7:])

# String methods-used to manipulate strings
# Upper and Lower case
print(fullname.lower())
print(fullname.upper())
# Length of a string-used sana sana in passwords for user to input a password with 8/more characters
print(len(fullname))
# Count-gets the number of appearances of  a character
print(fullname.count("a"))
# Strip
m="    bread    "
print(len(m))
stripped=m.strip()
print(stripped)
print(len(stripped))

# Split-used to remove leading and trailing spaces
# Replace(can be used in forgot password in real life)
n="     bread   ."
print("Length of n is: " ,len(n))
# Find-finds the character being looked for and returns the FIRST index of the character,if the character
# does not exist,it returns -1
print(fullname.find("N"))
# Capitalize
