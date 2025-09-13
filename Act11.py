print("Temperature Reader")

a = input("Pls Input Temperature --> ")

if a <= "0":
	print("Temperature is Freezing point")

elif a <= "20":
	print("Temperature is Cold")
elif a <= "30":
	print("Temperature is Warm")
elif a <= "49":
	print("Temperature is Hot")
else:
	print("Temperature is Super Hot")