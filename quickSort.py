array = [3,2,1,5,6,4]

def partition(array, p, q):
    x = array[p]
    i = p
    for j in range(p+1,q,1):
        if array[j]<=x:     #这里大于还是小于极易写错，可以这么想变动的指针只要更小就替换固定位置的大值
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i],array[p] = array[p],array[i]
    return i     

def quickSort(array, p, q):
    if p<q:
        r = partition(array,p,q)
        quickSort(array,p,r-1)
        quickSort(array,r+1,q)
    return array

print(quickSort(array,0,len(array)))
