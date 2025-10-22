for i in range(1,7,1):
    for c in range(7,i,-1):
        print(" ", end=" ")
    for d in range(1,i,1):
        print(d, end=" ")
    for x in range(1,i + 1,1):
        print(x, end=" ")
    print()