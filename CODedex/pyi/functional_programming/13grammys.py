# CODedex/pyi/functional_programming/13grammys.py
'''
* Author: TanB
* Created: 8/11/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

from functools import reduce

#map
def divide_b_2(x):
    return x/2
    

halved_num =map(divide_b_2, [1,2,3,4,5])

print(list(halved_num))

#filter
def filter_even(x):
    return x % 2==0
even_num = filter(filter_even, [1,2,3,4,5,6])

print(list(even_num))

#reduce 
def multiply(x,y):
    return x*y
product = reduce(multiply, [1,2,3,4,5])

print(product)

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02),
             ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_5_mins(musik):
    return musik[1] > 5.00

song5 = filter(longer_than_5_mins, playlist)

print(list(song5))

def mins_2_secs(songz):
    name = songz[0]
    seconds = songz[1] * 60
    return (name, seconds)

playlist_sec = map(mins_2_secs, playlist)

print(list(playlist_sec))

def add_dura(total, songz):
    return total + songz[1]

total_time = reduce(add_dura, playlist, 0)

print(f'This playlist es {total_time} mins long')