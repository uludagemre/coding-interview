from .utils import *


"""
Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that 
does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should 
give 3.

You can modify the input array in-place.
"""
def find_missing(arr: list) -> int:
    if isinstance(arr, str):
        arr = str2list(arr, int)

    arr_len = len(arr)
    
    for i, x in enumerate(arr):
        if x <= 0 or x > arr_len:
            arr[i] = 1

    for i in range(arr_len):
        arr[(arr[i] - 1) % arr_len] += arr_len

    for i, x in enumerate(arr):
        if x <= arr_len:
            return i + 1

    return arr_len + 1
