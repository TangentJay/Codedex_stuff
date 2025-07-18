# projects/areaCalculator.py
'''
* Author: TanB
* Created: 7/10/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#import math for more accuracy / also loads math module into memory
import math


print('++++===----*****///=====')
print('📏Area Calculator 📐')
print('++++===----*****///=====')

#Using a while loop with True. This es telling the computer to keep repeating the code that follows untill I tell you to stop
while True:
    print('******½****')
    print('1) Circle')
    print('2) Square')
    print("3) Rectangle")
    print('4) Triangle')
    print('5) Quit')
    

    #we will add the input function for users to select their choices
    #stores the user's choice in the variable choice
    choice=input('\nWhich shape would you like to calculate from 1-5?: ')

    #if statement for the selected choice und the code will run inside the select choice block
    #remember the number from input is a string and not a number
    if choice == '1':
        #circle area ist π * radius**2
        #Useres will input their values to be calculated
        radius = float(input("radius: "))
        area = math.pi * (radius ** 2)#We can use 3.14, we will use math.pi for more accuracy
        print(f'The area of the circle ist {area}')
    
    #elif means else + if
    elif choice == '2':
    # area of a square is s**2 or side squared
    # remember, it's hip to be square
        side = float(input('Enter the sides of the square: '))    
        area = side **2
        print(f'The area of the square ist {area}')
   
   #area of the rectangle es length * width
    elif choice == '3':
        length = float(input('Please entre der length:'))
        width = float(input('Please enter la width: '))
        area = length * width
        print(f'the area of la rectangle ist {area} ')
    
    elif choice == '4':
        #teh area of a triangle ist (base * height) /2 or 1/2 (b * h) same thing
        base=float(input('Please enter teh base: '))
        height=float(input('please enter teh height: '))

        area =(base * height) /2
        print(f'The area of teh TRIangle ist {area}')

    elif choice == '5':
        #exit the program
        print('La8ter G8ter')
        #I forgot to add break, haha! 
        break   # <- DOn't forget about break to exit the while loopz 
    
    else:
        #for invalid choices
        print('please enter a valid choice! 1-5.')
        
        






