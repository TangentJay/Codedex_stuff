# Codedex_stuff/projects/gif_py.py
'''
* Author: TanB
* Created: 7/5/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
# Codedex_stuff/projects/gif_py.py
'''
* Author: TanB
* Created: 7/5/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import imageio.v3 as io



filenames = ['naruto_74_640.jpg','lain_87_640.jpg','logic.jpg','albertE.jpg']
images = [ ]
target_shape=None



for filename in filenames:
    images.append(io.imread(filename))

io.imwrite('rnd.gif', images, duration=420, loop=0)
#imwrite() takes 4 functions. the name you want to give the gif. the list containg teh data. teh duration und teh loop(how many times to repeat)

