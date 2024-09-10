counter = 0 
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
choice = "awesome"
if age > 12 or age < 65 or choice == "awesome":
    print("You are tall and old enough to ride the roller coaster.")
    counter += 1   # counter = counter + 1
else:
    print("You are not tall enough or old enough to ride the roller coaster.")
        # messed up the logic of it all. 