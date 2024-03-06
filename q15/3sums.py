from bisect import bisect_left
from collections import defaultdict

class Solution(object):

    def bsearch(self, nums, find) -> int:
        i = bisect_left(nums, find)
        if i != len(nums) and nums[i] == find:
            return i
        return -1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        klst = defaultdict(int)
        sumlst = []

        for i in nums:
            klst[i] += 1
        
        nums = []
        for key, val in klst.items():
            nums += [key] * min(3, val)

        nums.sort()

        # add two numbers in array
        # find if number needed to make 0 is in the array
        total = len(nums)
        for a1 in range(0, total):
            for a2 in range(a1 + 1, total):
                need = -(nums[a1] + nums[a2])

                # binary search of needed number
                idx = self.bsearch(nums, need)
                
                # add all repeat occurrences of needed number
                if idx != -1:
                    while idx < total and nums[idx] == need:
                        if idx > a2 and [nums[a1], nums[a2], nums[idx]] not in sumlst:
                            sumlst.append([nums[a1], nums[a2], nums[idx]])
                                
                        idx += 1
        
        return sumlst 

obj = Solution()
nums = [-1,0,1,2,-1,-4]
print(obj.threeSum(nums))




        
