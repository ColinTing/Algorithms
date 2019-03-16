import random

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums)==0:
            return nums
        nums = self.quickSort(nums,0,len(nums)-1)
        return nums[k-1]
       
        
    def partition(self,nums,p,q):
        ra = random.randint(p,q)
        nums[p],nums[ra] = nums[ra],nums[p]
        x = nums[p]
        i = p
        for j in range(p+1,q+1,1):
            if nums[j]>=x:  #左边是nums[j]而不是nums[i]
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
        nums[p],nums[i] = nums[i],nums[p]
        return i

    def quickSort(self,nums,p,q):
        if p<=q:
            r = self.partition(nums,p,q)
            self.quickSort(nums,p,r-1)
            self.quickSort(nums,r+1,q)
            return nums

list = [3,2,1,5,6,4]
k = 2
s = Solution()
print(s.findKthLargest(list,k))