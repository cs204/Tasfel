fruit = input("Фрукт: ").lower()
fruits = {
"apple": 130,
"lime": 20,
"avocado": 50,
}

if fruit in fruits:
    calories = fruits[fruit]
print(f"Калории: {calories}")