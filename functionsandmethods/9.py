def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo(42, 3.141592, 2.718)
# It will print 42, 3.141592, and 2.718. While there are default arguments for second and third parameters, those argument takes place only if no argument for such parameter is given.
