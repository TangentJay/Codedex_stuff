# Write code below 💖

#21 21 21

"""
 Congrats!
You've made it to the end of this chapter! Let's do a recap. 🥳

The while loop iterates over and over again while the condition is true:

The for loop and the range() function to iterate for a certain number of times:

Fizz Buzz is a children's word game that teaches division.
It's also a classic technical interview question at countless companies. 🐝

Though this challenge may appear simple to experienced coders, 
it is designed to weed out 90% of job ~ 
candidates who cannot apply their coding knowledge to a new problem creatively. Want to give it a try?

Create a fizz_buzz.py program that outputs numbers from 1 to 100.

Here's the catch:

For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

oh! num % x==0
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz


"""
for num in range(1, 101):

    if num % 3 == 0 and num % 5 == 0:
        print('FIzzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)  
    
#wow! passed
