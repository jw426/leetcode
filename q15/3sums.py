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

        # storing the occurrences of numbers in dictionary
        for i in nums:
            klst[i] += 1

        totlst = list(klst.items())

        for i in range(len(totlst)):
            key, val = totlst[i]
            
            for j in range(i+1, len(totlst)):
                key2, _ = totlst[j]
                klst[key] -= 1
                klst[key2] -= 1
                if klst[-(key + key2)] > 0:
                    add = sorted([key, key2, -(key + key2)])
                    if add not in sumlst: 
                        sumlst.append(add)
                    
                klst[key] += 1
                klst[key2] += 1
                    
        return sumlst 

obj = Solution()
nums = [-1,0,1,2,-1,-4]
print(obj.threeSum(nums))




        
