def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo(42)
# It will print 42, 3, 2. Since there are no arguments for second and third parameters, default argument 3 and 2 will take place.
