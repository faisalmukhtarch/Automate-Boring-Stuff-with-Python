myPets = ["Zophie", "Mitty", "Fatty"]
print("Enter a pet name:")
name = input()
if name not in myPets:
    print("I dont have a pet named: " + name)
else:
    print(name + " is my pet")
