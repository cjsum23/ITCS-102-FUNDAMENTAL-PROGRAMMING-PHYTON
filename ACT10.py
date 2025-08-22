a = input("Pls Input Your Name -->")
b = input("Are you a student? (YES/NO)-->")
c = eval(input("Input Fare -->"))
d = c * .2
e = c - d

if b.lower() == "YES" :
    
     print ("You Pay", c,"\n Your discount is", d, "\n Your New fare is", e)

else:
 print("You are not alegible for the discount")