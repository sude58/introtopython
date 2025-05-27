foo = "bar"


def set_foo():
    foo = "qux"


set_foo()
print(foo)

# It will print bar since foo is defined as bar in global scope. While it is redefined as qux after, it only redefined in function scope.
