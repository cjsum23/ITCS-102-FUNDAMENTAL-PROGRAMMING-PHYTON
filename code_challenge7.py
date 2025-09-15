a = 0

for i in range(10):
    b = eval(input("Input Numbers --> "))

    if b % 2 != 0:
        a += b

        print("Total of odd numbers --> ", a)