def long_cap(characters):
    if len(characters) > 10:
        return characters.upper()
    else:
        return characters


print(long_cap("goodbye"))
print(long_cap("hello world"))
