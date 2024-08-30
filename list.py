# Lists is a data container that holds more than 1 variable. They need NOT be of the same Datatype.
# Imagine fetching data from a row in a database. For example you can have records belonging to a person in a list.
# A list is defined using square brackets and each value is referenced using an index starting from 0, 1, 2 and so forth.
# Example is: person = [“John Doe”, 30, “john@mail.com”, “Nairobi”]
# To access the name we use: person[0]
#  To access the age: person[1]

# TASK: Create a List of days of the Week. Print the day today using an index.
days_of_the_week=["Monday","Tuesday","Wednesday",[1,2,3,["a","b"],4],"Thursday","Friday","Saturday","Sunday"]
print("Today is: " + days_of_the_week[2])
print( days_of_the_week[3][2])
print( days_of_the_week[3][3][1])

# slicing
print(days_of_the_week[0:3])
# print(days_of_the_week["start":"end":"action"])
# If I want to display alternating days
print(days_of_the_week[0::2])
# If I want to display Monday and Wednesday only
print(days_of_the_week[0:3:2])
# If I want to display Thursday to Monday(-1 reverses)
print(days_of_the_week[4::-1])


# Modifying
days_of_the_week=["Monday","Tuesday","Wednesday",[1,2,3,["a","b"],4],"Thursday","Friday","Saturday","Sunday"]
days_of_the_week[2]="January"
print(days_of_the_week)

# Length
print(len(days_of_the_week))

# max()
# max(a[2:4] + ['grault'])
# 'qux'
# a[2:4] returns the slice ['baz', 'qux']. The + operator concatenates, so the argument to max() is ['baz', 'qux', 'grault']. The maximum value (for strings, the latest in alphabetical order) is 'qux'.
