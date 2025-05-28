stuff = ("hello", "world", "bye", "now")
print(stuff)
# Impossible. Since tuple is immutable, you cannot change element of tuple. You can create new tuple with goodbye instead.
stuff = list(stuff)
stuff[2] = "goodbye"
stuff = tuple(stuff)
print(stuff)
# Solution with spirit of the exercise.
