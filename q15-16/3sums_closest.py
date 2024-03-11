import sys
from bisect import bisect_left

class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # base case 
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        cursum = sum(nums[0:3])

        for i in range(len(nums) - 2):
            low, high = i+1, len(nums) - 1
            
            lowest = sum(nums[i:i+3])
            highest = nums[i] + nums[-1] + nums[-2]
            
            if target < lowest:
                if abs(target - cursum) > abs(target - lowest):
                    cursum = lowest
                continue
        
            if target > highest:
                if abs(target - cursum) > abs(target - highest):
                    cursum = highest
                continue

            # disregard repeating 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while low < high:
                cur = nums[i] + nums[low] + nums[high]
                if cur > target:
                    high -= 1
                elif cur < target:
                    low += 1
                # target can be achieved
                else:
                    return cur
                
                if abs(target - cursum) > abs(target - cur):
                    cursum = cur
            
        return cursum


