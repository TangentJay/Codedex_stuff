# Codedex_stuff/KhanaStuff/Lessons.py
'''
* Author: TanB
* Created: 7/3/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
base_price=float(input('Entre cart total: '))
shipping_cost=float(input('Entre shipping cost: '))
#available coupon codes includes 15%off und $12 off
percent_discount=base_price - base_price * .15
fixed_discount= base_price - 12

#pick the coupon that offers the best discount
final_price =min(fixed_discount, percent_discount) + shipping_cost
print('dein best price es $' + str(round(final_price,2))) #Round the final price to two decimal places.

