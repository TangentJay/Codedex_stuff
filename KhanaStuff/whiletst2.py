# 9,1,2025

import random
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = iris

print(df.head())

# pin = ''

# while len(pin) < 4:
#     print(pin)
#     digit = random.randint(0,9)
#     pin = pin + str(digit)
    
# print(f'your pin es {pin} ')