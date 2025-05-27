# Reassignment and mutation
"""
obj = 'ABcd'  # Reassignment
obj.upper()  # Neither, it does not mutate original
obj = obj.lower() Reassignment, it reassigns obj into returned value of lower()
print(len(obj)) # Neither, it just measures length of obj
obj = list(obj) # Reassignment, it returns list that is constructed using the original obj and assigns to new variable
obj.pop() # Mutation, it deletes the last character in string
obj[2] = 'X' # Mutation, it changes one of index of obj
obj.sort() # Mutation, since it sorts list in order
set(obj)  # Neither, it just creates new set using obj
obj = tuple(obj) # Reassignment, t returns tuple that is constructed using the original obj and assigns to new variable
"""
