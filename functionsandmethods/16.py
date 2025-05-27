def multiply(left, right):
    return left * right


def get_num(prompt):
    return float(input(prompt))


first_number = get_num("Enter the first number: ")
second_number = get_num("Enter the second number: ")
product = multiply(first_number, second_number)
print(f"{first_number} * {second_number} = {product}")
# Function names and parameters
"""
Function names
multiply 1 (defined), 9
get_num 4 (defined), 7, 8
Parameters
left, right 1 (defined), 2
prompt 4 (defined), 5
"""
