min_sum = int(input("Введите сумму минимальную сумму инвестиций "))
money_m = int(input("Введите колличество долларов Майкла "))
money_i = int(input("Введите колличество долларов Ивана "))
if money_m >= min_sum and money_i >= min_sum:
	print("2")
elif money_m >= min_sum:
	print("Mike")
elif money_i >= min_sum:
	print("Ivan")
elif (money_m + money_i) >= min_sum:
	print("1")
elif money_m < min_sum and money_i < min_sum:
	print("0")
