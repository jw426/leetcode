class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ndct = {}   # dictionary stores (key, number of occurrences of key)
        sumlst = [] # return list

        # storing the occurrences of numbers in dictionary
        for i in nums:
            if i not in ndct: 
                ndct[i] = 0
            ndct[i] += 1

        totlst = sorted(list(ndct.keys())) # distinct numbers in order

        for i in range(len(totlst)):
            key1 = totlst[i]
            # to indicate use of variable 
            ndct[key1] -= 1
            
            for j in range(i, len(totlst)):
                key2 = totlst[j]
                # for duplicate occurrences of a number
                if ndct[key2] <= 0: 
                    continue
            
                # to indicate use of variable 
                ndct[key2] -= 1
                cmpl = -(key1 + key2) 

                # to prevent repeats in return list
                if cmpl >= key2 and cmpl in ndct:
                    if ndct[cmpl] > 0:
                        sumlst.append([key1, key2, cmpl])
                
                # revert to original state after use
                ndct[key2] += 1

            # revert to original state after use
            ndct[key1] += 1
                    
        return sumlst 





        
