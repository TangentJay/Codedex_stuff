# projects/chaos.py
'''
* Author: TanB
* Created: 7/6/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
# a simple program illustrating chaotic behavior

#def the main function

def main():
#printed the message of what this program does
    print('This program illustrates a chaotic function')
    x=float(input('Entre a numbre between 0 und 1: '))

     #use a for loop to run the chaotic formula x10
    for i in range(10):
        #update x using llogistic map: x=r*(1-x)
        # hier r es 3.9, which causes chatic behavior in this formula
        x=3.9 * x * (1-x)
        
        #print the current value if x after each calculation
        print(x)

main()   