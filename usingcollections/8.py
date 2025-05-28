text = "It's probably pining for the fjords!"

print(text[21:35].rfind("f"))  # 8
print(text.rfind("f", 21, 35))  # 29

# While rfind finds the exactly same character in exactly same position, 29th in the original string, on line 3,
# rfind was executed on substring starting on 21th character, which changes relative position of the character.
