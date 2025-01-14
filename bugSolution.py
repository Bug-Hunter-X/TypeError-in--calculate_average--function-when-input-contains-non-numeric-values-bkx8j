def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle case where all elements are non-numeric
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_mixed_list = [1, 2, 'a', 4, 5]
average_mixed = calculate_average(my_mixed_list)
print(f"The average of a mixed list is: {average_mixed}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_non_numeric_list = ['a', 'b', 'c']
average_non_numeric = calculate_average(my_non_numeric_list)
print(f"The average of a non-numeric list is: {average_non_numeric}"