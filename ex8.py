# ex8.py
'''
* Author: TanB
* Created: 7/15/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
form = '{} {} {} {} {} {} {}' 

#saving {} format value to a variable and using teh print function with .format to add in values
print(form.format('one', 'Two', 'Three', 'Four', 'Five', "Six",'7'))
print(form.format(1,2,3,4,5,6,7))
print(form.format(True,False,False,True ,False, False,True))
print(form.format(form,form,form,form,form,form,form)) #printing out {} *7 times so total = 49
print(form.format("Money", 
    "comes", 
    'to, meh',
    'always',
    'und',
    'forever!',
    'Und Ever'

))