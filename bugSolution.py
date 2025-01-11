def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_numbers = []
result = calculate_average(my_numbers)
print(f"Average: {result}") # Output: Average: 0

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"Average: {result}") # Output: Average: 30.0

my_numbers = [10, 20, 'a', 40, 50]
result = calculate_average(my_numbers)
print(f"Average: {result}") # Output: Average: 30.0