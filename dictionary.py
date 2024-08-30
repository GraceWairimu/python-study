# Let say you have a very large list/tuple for you to access values you have to count through the index. This can become very hard and impossible for large lists. 
# Therefore dictionaries solve this using key:value pairs. Defined inside curly braces.
# Please note that a key can not be repeated in a dictionary. If you define a key and try to create another, the previous value will be replaced.
# Keys are case sensitive i.e  “Name” is different from “name”.
# A value in a dictionary can be of any datatype, but the key always has to be string. 

# Creating a dictionary
person={
    "name" : "Grace",
    "age" : 21,
    "location" : "Muthiga"
}

# Accessing values in a dictionary
print(person["name"])
print(person["location"])

# Adding elements in a dictionary
person["city"]="Nairobi"
print(person)
person["units"]=["OOP","Operating System","Algebra"]
print(person)
# Updating elements
person["location"]="Ruai"
print(person)

person={
    'name': 'Grace', 
    'age': 21,
    'location': 'Ruai', 
    'city': 'Nairobi', 
    'units': ['OOP', 'Operating System', 'Algebra'],
    "adr":{
        "code":20200,
        "str":"kimathi"
    }
}
print(person["units"][1]) #getting Operating System
print(person["adr"]["str"])  #accessing the street Kimathi
person["units"].append("HTML") #used to add html to the key "units" which is a list
print(person)
person["units"].remove("OOP") #used to remove OOP from the key "units" which is a list
print(person)
person["adr"]["town"]="Nairobi"  #adding town in the dictionary "adr"
print(person)
person["adr"]["str"]="moi avenue"  #updating "str" from kimathi to moi avenue
print(person)

# METHODS
# .keys()-used to display all the keys in a dictionary
print(person.keys())

# .values()-used to display all the values in a dictionary
print(person.values())

# .items()-used to display all the key:value pairs in a list of tuples
print(person.items())

# .clear()-clears everything
# .copy()-duplicates data inside a dictionary on another
# .get()
print(person.get("name"))
# .pop()
print(person.pop("name"))
# .popitem()

# not nccessary for the keys to be of the type strings
dict={
    1:"ginger"
}
print(dict[1])