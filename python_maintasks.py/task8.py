# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

# speed=int(input("Enter the speed: "))
# speed_limit=70
# demerit_point=0

# if speed<speed_limit:
#     print("OK")
# else:
#     demerit_point=((speed-speed_limit)//5)
#     print(f"The demerit point is {demerit_point}")
# if demerit_point>12:
#     print("License suspended")

    # OR
speed=int(input("Enter the speed: "))
speed_limit=70
demerit_point=0

if speed<=speed_limit:
    print("OK")

elif speed>speed_limit and speed<=75:
    demerit_point+=1

else:
    demerit_point=1
    demerit_point+=round((speed-75)/5)
    if demerit_point>12:
       print("License suspended")
    else:
        demerit_point=demerit_point

print(f"The demerit point is {demerit_point}")




