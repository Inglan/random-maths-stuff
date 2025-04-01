import math

result = 2

for i in range(2, 690):
    result = result + (1/math.factorial(i))

print(result)