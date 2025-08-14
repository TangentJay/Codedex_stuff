# projects/guido.py
'''
* Author: TanB
* Created: 8/8/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    
    """
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    



def preparation_time_in_minutes(number_of_layers):
    """
    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes), based on 2 minutes per layer.

    Calculates the total preparation time by multiplying the number of layers
    by the time each layer takes to prepare.
    """
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    :param number_of_lyers: int - the number of layers in the lasagna
    :param elapsed_bake_time: int - bake time already elapsed
    :return: int - total time (minutes) spent preapring and baking.

    Calculates the total elapsed cooking time by adding preparationtime
    (based on the number of layers) to the baking time that already passed
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(elapsed_time_in_minutes(4,40))
print(preparation_time_in_minutes(1))
print(bake_time_remaining(1))

xy = 2
print(xy)