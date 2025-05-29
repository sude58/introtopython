set1 = {42, "Monty Python", ("a", "b", "c")}
set2 = set1
set1.add(range(5, 10))
print(set2)
"""
It will print a {42, "Monty Python", range(5,10), ("a", "b", "c")}. Since set2 and set1 are same object, change in set1 will be reflected on set2 too.
"""
