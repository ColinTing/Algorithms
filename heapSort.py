def left(i):
    return 2*i

def right(i):
    return 2*i+1

def max_heapify(A,i):
    l = left(i)
    r = right(i)
    if l<=len(A) and A[l-1]>A[i-1]:
        largest = l
    else:
        largest = i
    if r<=len(A) and A[r-1]>A[largest-1]:
        largest = r
    if largest != i:
        A[i-1],A[largest-1] = A[largest-1],A[i-1]
        max_heapify(A,largest)

A = [4,1,3,2,16,9,10,14,8,7]

B = []
#这只是在建最大堆。。。
for i in range(int(len(A)/2),0,-1):
    max_heapify(A,i)

#踢出最大值
for i in range(len(A),1,-1):
    A[0],A[len(A)-1] = A[len(A)-1],A[0]
    B.append(A.pop())
    max_heapify(A,1)
B.append(A.pop())
print(B)


