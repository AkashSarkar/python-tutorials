# list comprehensions
numbers = [23, 34, 55, 65, 44, 66, 32, 22, 26, 30, 18, 78]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)

