import math, decimal
from decimal import *

getcontext().prec = int(input("Precision: "))

result = Decimal(0)

for i in range(0, getcontext().prec+2):
    print(f"\rCalculating {i}/{getcontext().prec+2}      ", end="")
    result = result + Decimal(1/math.factorial(i))

print(result)