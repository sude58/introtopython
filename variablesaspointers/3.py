dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    "Monty Python": "The Life of Brian",
    "Airplane!": "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2["Monty Python"] = "Holy Grail"
print(dict1["Monty Python"])
"""
It will print "The Life of Brian" 
Since using constructor of same type creates a shallow copy, dict2 and dict1 are different object. So change in dict2 will be not reflected on dict1.
"""
