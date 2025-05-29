dict1 = {
    "a": [1, 2, 3],
    "b": (4, 5, 6),
}

dict2 = dict(dict1)
dict1["a"][1] = 42
print(dict2["a"])
"""
It will print [1, 42, 3] 
Since using constructor of same type creates a shallow copy, nested collections in two dicts are same object. 
So change in nested list at dict2 will be reflected on dict1's nested list too.
"""
