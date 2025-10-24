a = []
b = True

while b == True:
    c = input("Enter anime (type 'exit' to Stop)-- ").lower()
    if c == "exit":
        print("\nYour list of anime:")
        break

    a.append(c)
    print(f"{c} has been added to your anime list.")

for i in a:
    print(f"- {i}")
    