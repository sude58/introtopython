# Modified age.py
age = int(input("How old are you? "))
future = [10, 20, 30, 40]
print(f"You are {age} years old")
for year in future:
    print(f"In {year} years, you will be {age + year} years old.")
