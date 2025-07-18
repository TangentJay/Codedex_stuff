# KhanaStuff/bompoundb.py
'''
* Author: TanB
* Created: 7/13/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#Compound boolean expressions
'''
operator	operation	example  	asks
not	        negation	  not x	   is x not True? :  The not operator negates the result of any boolean expression. not T=F, not F=T
and	      conjunction	x and y	   are all of x and y True?  A boolean expression with the and operator only evaluates to True if both conditions evaluate to True. T and T = F. F and T = F. T and F = F. F and F = T
or	      disjunction	x or y	  are any of x or y True? A boolean expression with the or operator evaluates to True if at least one condition evaluates to True.  T or F = T. F or T = T. F or F = F. T or T = T
'''
genre = 'lo-fi' 
bpm = 126

#match target running pace to the beats per minute
is_running_song = bpm >= 150 and bpm <= 180
print(f'are the beats per minute between? {is_running_song}')

#count alternative spellings of lo-fi as a single genre
is_lo_fi = genre == 'lo-fi' or genre == 'low-fi' or genre == 'lofi'
print(f'Is the genre any of the spellings of lo-fi? {is_lo_fi}')

"""

if is_running_song == False:
    print('not lo fi')
else:
    print('is lo-fi')    
"""

# chill background music 
is_study_song = is_lo_fi and bpm < 100
if is_study_song:
    print("this slow, lo-fi song is perfect for studying")
else:
    print('where song')    

#don't play activity-specific at other times of the day
if not is_study_song and not is_running_song:
    print('This is not one of my study songs')  
