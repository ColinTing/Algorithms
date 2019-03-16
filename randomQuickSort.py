import random


def partition(array, p, q):
    ra = random.randint(p,q)
    x = array[ra]
    #随机数交换到开头必不可少
    array[p],array[ra] = array[ra],array[p]
    i = p

    for j in range(p+1,q+1,1):  #range的起点是p+1
        if array[j]<=x:     #等于号也加上
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i],array[p] = array[p],array[i]
    return i


def quickSort(array, p, q):
    if p<q:                         #要有边界判断
        r = partition(array,p,q)
        quickSort(array,p, r-1)
        quickSort(array,r+1,q)
        return array



array = [3,2,1,5,6,4]
result = quickSort(array,0,len(array)-1)
print(result)