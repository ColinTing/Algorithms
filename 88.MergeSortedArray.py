class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1
        j = n-1
        k = m+n-1

        while k>=0 and i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        if j>=0:
            nums1[:j+1]=nums2[:j+1]     #列表是[]闭开区间，所以j需要加1
        return nums1

s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
print(s.merge(nums1,m,nums2,n))