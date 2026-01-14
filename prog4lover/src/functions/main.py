# def  functions_name(parameters):

# the definition of a function can occur in any order

# but.. when executions are executed, definitions mmust have already been encountered

def main():
    print('functions in python')

    x = 3

    n = sum_two_ints(x, 8)
    print(f'the sum of 3 and 8 is, {n}')


def sum_two_ints(a:int, b:int):
    """
    Docstring for sum_two_ints
    return the sum of two input interger
    :param
    -a (int)
    -b (int)

    """
    return a+b  #output of the function

def print_hi():
    """
    Docstring for print_hi

    takes input and simply return hi
    """
    print("hi")


#functions can also return more than one value
def double_and_duplicate(x: float):
    
    """
    Double the input variable and return two copies of it

    
    :param 
    -x (float)
    
    returns:
    two copy of 2x
    """
    return 2*x, 2*x
    print(double_and_duplicate(2.7))

"""
special function that takes no input, produces no outputs but that constitutes the runnable componet of our program
"""

def add_one(k: int) -> int:
    """
    Docstring for add_one
 to the input variable and return results    
    :param k: Description
    :type k: int
    :return: Description
    :rtype: k+1
    """
    k = k+1
    return k + 1
# left side is variable, the rightside is the value.  k = 1

if __name__ == "__main__":
    main()
    
        