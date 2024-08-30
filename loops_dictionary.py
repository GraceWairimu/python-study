# =>When looping through a dictionary we Iterate over the keys and values of a dictionary:
# example:person={“name”:”Techcamp”,”age”:25,”city”:”Nairobi”}
# for key,value in person.items():
# 	print(key,value )#displays all items
# =>looping through keys alone you use person.keys()
# example:for key in person.keys():
# 	print(key)#loops through all the keys
# =>looping through values alone you use person.values()
# for key in person.keys():
# 	print(key)#loops through all the keys
# NB:Looping through multiple sequence you use  Zip inbuilt  function 

# ----------------------------------------------------------------------------------------------
person={
     "name":"kevin",
     "age":25,
     "city":"newyork"
    
}
# -----------------------------------------------------------------------------------------------
# loop through items(keys and values)-perszon.items()
for i,x in person.items():
    # print(i,x)
    # OR
    print(f"{i}:{x}")
# ------------------------------------------------------------------------------------------------
# loop through keys
for keys in person.keys():
    print(keys)
# -------------------------------------------------------------------------------------------------
# loop through values
for values in person.values():
    print(values)
# -----------------------------------------------------------------------------------------------
# looping through 2 dictionaries using zip
person={
     "name":"kasuku",
     "age":25,
     "city":"newyork"
    
}
person1={
     "name":"grace",
     "age":21,
     "city":"nairobi"
    
}

for (key,value),(key1,value1) in zip(person.items(),person1.items()):
    # print(key,value,key1,value1)
    # OR
    print(f"{key}:{value}:  {key1}:{value1}")