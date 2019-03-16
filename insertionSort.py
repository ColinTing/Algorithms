arr = [8,2,4,9,3,6]

for j in range(1, len(arr), 1):
    key = arr[j]
    i = j-1
    while i>=0 and arr[i]>key:  #arr[i]>key 还是 arr[i]<key  分不清
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = key

#这里竟然写了return,这里又没有定义个方法，写哪门子返回

print(arr)
        


