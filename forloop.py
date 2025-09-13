while True:
    a = int(input("Input Howmany lines of * -->"))

    for i in range(1, a + 1):
        print(" " * (a - i), end="")
    
        for x in range(0, i):
            print("*", end=(" "))
        print(" ")

    again = input("Do you want to Try again? (Yes/No) --> ").lower()

    if again != "yes":
        print("Thank You")
        break

        #if i in range(a):
            #print("* " * a)
        #print()