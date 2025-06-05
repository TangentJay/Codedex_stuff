# Write code below 💖
"""
acidity= level of acid in a substance 
basicity =  quality of being base, not an acid
scale of 0~14 |  ph < 7 = acid und  > 7 =basic
"""
ph=float(input("Entre the ph value between 0 and 14:  "))

if ph == 7:
    print('Es Neutral ')
elif ph < 7:
    print('Es Acidity ')
else:
    print('Basicity')