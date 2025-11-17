isDirty = True

while isDirty == True:
    a = input("Continue The Cycle? (yes/no) --> ").lower()

    if a == "yes":
        print("The cycle continue :>")
        continue
    elif a == "no":
        print("The cycle stops :<")
        break
    else:
        print("Invalid Input ??")
        continue