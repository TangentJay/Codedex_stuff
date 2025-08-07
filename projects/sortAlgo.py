# projects/sortAlgo.py
'''
* Author: TanB
* Created: 8/6/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index



def selectionsort(arr):
    newArr = []
    copiedArr = list(arr) # it says copy array before mutating, but I dont understand
    for i in range(len(copiedArr)):
        smallest = findsmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr
print(selectionsort([5,3,6,2,10]))