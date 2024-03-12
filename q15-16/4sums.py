class Solution(object):

    # modified from threeSumClosest in 
    # 3sums_cloeset.py in current folder
    def fourSum(self, nums, target):

        nums.sort()
        res = []     # we return this array
        
        # n1
        for i in range(len(nums)):

            # disregard repeating 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # n2
            for j in range(i+1, len(nums) - 2):
                # n3, n4
                low, high = j+1, len(nums) - 1

                # target can never be achieved with current i and j
                if target < nums[i] + sum(nums[j:j+3]):
                    break
                if target > nums[i] + sum(nums[-3:]):
                    break

                # disregard repeating 
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                while low < high:
                    curcomb = [nums[i], nums[j], nums[low], nums[high]]
                    if sum(curcomb) > target:
                        high -= 1
                    elif sum(curcomb) < target:
                        low += 1
                    else:
                        res.append(curcomb)
                        low += 1
                        while low < high and nums[low] == nums[low - 1]:
                            low +=1 

        return curcomb

obj = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(obj.fourSum(nums, target))
                
        