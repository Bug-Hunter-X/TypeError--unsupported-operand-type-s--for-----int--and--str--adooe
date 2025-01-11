def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_numbers = []
result = calculate_average(my_numbers)
print(f"Average: {result}") # This will print 0, which is expected

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"Average: {result}") # This will print 30.0, which is expected

my_numbers = [10, 20, 'a', 40, 50] # the bug is introduced here
result = calculate_average(my_numbers)
print(f"Average: {result}") # This will raise TypeError because of string in list
