import sys
from bisect import bisect_left

class Solution(object):

    # function to find the "number" (not index) of the closest value to find
    # using binary search O(logn)
    def bsearch_closest(self, nums, find) -> int:
        i = bisect_left(nums, find)

        # closest value to find is either min or max values in list
        if i == 0:
            return nums[i]
        if i == len(nums):
            return nums[i-1]
        
        
        # number required for making target is found
        if nums[i] == find: 
            return find
        # not found, compare with left and right values
        
        return nums[i-1] if find - nums[i-1] < nums[i] - find else nums[i]
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        res = sys.maxsize + target

        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                need = target - nums[i] - nums[j]
                closest_val = self.bsearch_closest(nums[j+1:], need)
                rescmp = closest_val + nums[i] + nums[j]
                if abs(rescmp - target) < abs(res - target):
                    res = rescmp

        return res
        
        