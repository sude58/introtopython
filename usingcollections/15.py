pets = {
    "Cat": "Meow",
    "Dog": "Bark",
    "Bird": "Tweet",
}

keys = pets.keys()
del pets["Dog"]
pets["Snake"] = "Sssss"
print(keys)  # dict_keys(['Cat', 'Bird', 'Snake'])
