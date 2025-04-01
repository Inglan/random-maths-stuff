import math, decimal
from decimal import *

getcontext().prec = 100

result = Decimal(2)

for i in range(2, getcontext().prec+3):
    result = result + Decimal(1/math.factorial(i))

print(result)