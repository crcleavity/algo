from typing import List

def bubblesort(a:List(int)):
    length = len(a)
    if length<=1:
        return List
    
    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j+1]:
                