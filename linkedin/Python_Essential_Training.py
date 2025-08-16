# linkedin/Python_Essential_Training.py
'''
* Author: TanB
* Created: 8/15/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
i = 0
s = 0

while i < 10:
    i = i + 1
    s = s + i

print(i,s)

def addnum(i):
    if i == 0:
        return 0
    return i + addnum(i - 1)

print(addnum(11))

def addNumbers(i):
    print(f'Entering addNumbers({i})')  # Shows when we call the function
    
    if i == 0:
        print('Base case reached: returning 0')
        return 0
    
    result = i + addNumbers(i - 1)  # Recursive call
    print(f'Returning {result} from addNumbers({i})')  # Shows what we return
    
    return result

# Run the function
total = addNumbers(10)
print(f'\nFinal result: {total}')




def fac(num):
    fac = 1
    counter = 1
    while counter <= num:
        fac = fac * counter
        counter +=  1
    return fac

print(fac(4))