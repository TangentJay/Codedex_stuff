# CODedex/pyi/numPY/10halley.py
'''
* Author: TanB
* Created: 7/24/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#.shape, /reshape
#.arange short for array range
#we can add parameters  np.arange(start=x, stop=y, step=z)

import numpy as np

#stop has an upper limit
arr = np.arange(start=0, stop=11,step=2)

print(arr)

Halley = np.arange(start = 1986, stop=3001 , step = 75)

#print(f'Halley\'s coment was last visible 1986, we will count by 75 years so next will be around: {Halley}')

print('Halles\'s COment is should show it\'s face in the following yrs: ' )
for year in Halley:
    print( year)