# Write code below 💖 6/5/2025
"""
import random

hunger=random.randint(0,9)
anger=random.randint(0,9)

if hunger >4 and anger >1:
    print('hangry')
else:
    print('good')    
print(hunger, anger)


if coffee < 4 or bubble_tea > 5:
  print('kooling')
"""

# logican operations 
"""
and returns True if both conditions are True, and returns False otherwise.
or returns True if at least one of the conditions is True, and False otherwise.
not returns True if the condition is False, and vice versa.
"""

Height=int(input("Ello, please entre dein height:  " ))
credits=int(input("Ello, how many credits ju have? "))


if Height >= 137  and credits >= 10 : # >=
    print(' Fun ✔ times!')
elif credits >= 10 and Height < 137 :
    print(' smol man, sorry too short!')
elif Height >= 137 and credits < 10 :
    print(' Not enough credits!')
else:
    print('Missing all the requirementz, Height und Credits')
