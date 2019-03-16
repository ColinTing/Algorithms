
matrix = [20, 12, 13, 11, 7, 9, 2, 1]


def halfCut(arr):
    if len(arr) == 1:
        return arr
    else:
        left = []
        right = []
        for i in range(0, int(len(arr)/2),1):
            left.append(arr[i])
        for j in range(int(len(arr)/2),len(arr),1):
            right.append(arr[j])
        left = halfCut(left)
        right = halfCut(right)

        i = 0
        j = 0
        for k in range(0, len(arr),1):
            if left[i]<right[j]:
                arr[k] = left[i]
                i += 1
                if i>=len(left):
                    break
            else:
                arr[k] = right[j]
                j += 1
                if j>=len(right):
                    break
        if i>=len(left):
            arr[k+1:len(arr)] = right[j:len(right)]   #k需要+1，不要只看到j，i都加1了而忘了k没+1
        if j>=len(right):
            arr[k+1:len(arr)] = left[i:len(left)]
        return arr

matrix = halfCut(matrix)
print(matrix)
