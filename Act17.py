a = int(input("Input Howmany lines of * -->"))

for i in range(1, a + 1):
        print(" " * (a - i), end="")
    
        for x in range(0, i):
            print(i , end=(" "))
        print(" ")