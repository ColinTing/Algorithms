def left(i):
    return 2*i

def right(i):
    return 2*i+1

#最大堆
def Max_heapify(A,i):
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
        Max_heapify(A,largest)


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #建堆
        for i in range(int(len(nums)/2),0,-1):
            Max_heapify(nums,i)
        
        for i in range(0,k,1):
            nums[0],nums[len(nums)-1] = nums[len(nums)-1],nums[0]
            largest = nums.pop()
            Max_heapify(nums,1)
        return largest

list = [3,2,3,1,2,4,5,5,6]
k = 4
s = Solution()
print(s.findKthLargest(list,k))





    
        

        