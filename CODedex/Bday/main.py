# Codedex_stuff/CODedex/Bday/main.py
'''
* Author: TanB
* Created: 6/25/2025
* Company: Oosode
'''
import datetime
import bday_messages

today=datetime.date.today()

this_year=today.year
next_birthday=datetime.date(this_year, 11,5)
 
if next_birthday < today:
     next_birthday=datetime.date(this_year + 1, 11,5)

days_away=(next_birthday - today).days

if today == next_birthday:
   print(bday_messages.random_message)
else:
 print(f'Mi next Bday es {days_away} days away 😧')
