import pandas as pd

"""1. Write a Python function that takes a list of integers and returns the sum of the even numbers
 in the list. e.g: list = [1,2,3,4,5]"""

test_numbers = [1, 2, 3, 4, 5, 6, 7]


def sum_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum


print(f"The sum of even numbers in the list is: {sum_even_numbers(test_numbers)}")
print("----------------------------------------------------------")

"""2. Write a Python code that will read the "test-1.csv" file and group all values by text columns
 present in the file."""

df = pd.read_csv('test-1.csv')
print(df.head())
print("----------------------------------------------------------")

# for instance, max value of Numeric1 for each group
print(df.groupby(['Text', 'AdditionalText']).agg(max_numeric1=('Numeric1', 'max')))

