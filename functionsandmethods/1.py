def set_foo():
    foo = "bar"


set_foo()
print(foo)

# It will raise a Nameerror since foo is a local variable and cannot be referenced in global scope.
