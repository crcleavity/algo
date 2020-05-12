from typing import List

def bubblesort(a:List(int)):
    length = len(a)
    if length<=1:
        return List
    
    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                made_swap = True
            if not made_swap:
                break

def insertion_sort(a):
    length = len(a)
    if length <= 1:
        return
    for i in range(1,length):
        value = a[i]
        j = i - 1
        while j>=0 and a[j] > value:
            a[j+1] = a[j]
            j -= 1
        a[j + 1] = value

def insertion_sort(a):
    length = len(a)
    if length <=1:
        return a
    for i in range(1,length):
        value = a[i]
        j = i - 1
        while j >=0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value

def selection_sort(a):
    length = len(a)
    if length <= 1:
        return a
    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

#依次从数组中找到最小值，放到第一位
#具体实现方法是，先找出找出第一个最小值，然后对后边依次遍历，找出最小值所对应的数值
#以及下标，然后进行更换
def selection_sort(a):
    length = len(a)
    if length <= 1:
        return a
    for i in range(length):
        min_index = i 
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_index = j
                min_val = a[j]
        a[i],a[min_index] = a[min_index],a[i]
    