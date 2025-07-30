# CODedex/pyi/binarys.py
'''
* Author: TanB
* Created: 7/25/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
def binaryS(arr, item):
    low = 0
    high = len(arr)-1


    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None


my_list = [1,3,5,7,9]
print(binaryS(my_list,3)) 
print(binaryS(my_list, -1))
    
