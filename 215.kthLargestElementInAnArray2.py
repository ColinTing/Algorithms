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
        nums = self.quickSort(nums,0,len(nums)-1,k)
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

    def quickSort(self,nums,p,q,k):
        if p<=q:
            r = self.partition(nums,p,q)
            if r == k-1:
                return nums
            if r < k-1:
                p = r+1
                return self.quickSort(nums,p,q,k)
            if r > k-1:
                q = r-1
                return self.quickSort(nums,p,q,k)

list = [3,2,3,1,2,4,5,5,6]
k = 4
s = Solution()
print(s.findKthLargest(list,k))