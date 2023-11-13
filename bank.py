def bank(costumer):
	if costumer.lower().startswith("здравствуйте"):
		return "$0"
	elif costumer.lower().startswith("з"):
		return "$20"
	else:
		return "$100"

costumer = input("Приветствие: ")
result = bank(costumer)
print(result)