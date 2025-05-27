def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
# It will raise an error since there is no argument given for third parameter and no default argument for that parameter exists.