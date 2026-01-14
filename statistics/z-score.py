# statistics/z-score.py
'''
* Author: TanB
* Created: 8/14/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
# Z-score: (data point - mean) / standard deviation
def zscore(d, m,s):
    return (d-m) /s

print(f"the z score es: {zscore(500, 300, 50)}")
#------------------------


def celsius_to_f(celsius):
    """convert celsius to fahrenheit"""
    return celsius * (9/5) 


def fahrenheit_to_c(fahrenheit):
    """convert fahrenheit to celsius"""
    return (fahrenheit) * 5/9

print(celsius_to_f(20))

print(fahrenheit_to_c(68))

std_c = 20
std_f = 68

std_f_c = fahrenheit_to_c(std_f) 

print(f"set 1 sd in c {std_c}")
print(f'set 2 sd in c {std_f_c:.2f}')

if std_c > std_f_c:
    print('set 1 has greater variability')
elif std_f_c > std_c:
    print('set 2 has greater variability')
else: print('even flow')

r = 25, 60, 95, 175, 195

def rangee(r):
    return max(r) - min(r)    

print(rangee(r))


some_set = 20, 200, 20, 140, 40, 20, 50
def meann(a):
    return sum(a)/len(a),
    
def med(a):
    sort_a = sorted(a)
    n = len(sort_a)
    mid = n //2 
    if n % 2 ==0:
        return(sort_a[mid-1]+ sort_a[mid]) /2
    else:
        return sort_a[mid]
    
def mode(a):
    counts = {}
    for x in a:
        counts[x] = counts.get(x,0)+1
    maxc = max(counts.values())
    modes = [o for o, u in counts.items() if u == maxc]
    return modes

# print(sum(some_set))
# print(some_set)
print('----------------------')
print(meann(some_set))
print(med(some_set))
print(mode(some_set))