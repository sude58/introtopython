def factorial(n):
    answer = 1
    counter = 1
    while counter <= n:
        answer *= counter
        counter += 1
    return answer


print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120
print(factorial(6))  # 720
print(factorial(7))  # 5040
print(factorial(8))  # 40320
print(factorial(25))  # 15511210043330985984000000
