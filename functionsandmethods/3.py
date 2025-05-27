def multiply(num1, num2):
    return num1 * num2


def get_number(prompt):
    return float(input(prompt))


a = get_number("Enter the first number: ")
b = get_number("Enter the second number: ")
print(f"{a} * {b} = {multiply(a, b)}")
