print(False or (True and False))  # False
print(True or (1 + 2))  # True
print((1 + 2) or True)  # 3, returns 3 since it is truthy and gets short circuit
print(True and (1 + 2))  # 3
print(False and (1 + 2))  # False
print((1 + 2) and True)  # True
print((32 * 4) >= 129)  # False
print(False != (not True))  # False
print(True == 4)  # False
print(False == (847 == "847"))  # True
