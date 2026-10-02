class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # finiding minimum index so that it divides the array into two ascending arrays : 

        l = 0 
        r = len(nums)-1

        while l < r : 
            m = (l+r)//2 

            if nums[m]> nums[r]:
                l = m+1
            else: 
                r = m 

        min_i = l #minimun index is here 

        # makng bounds for the binary search : 

        if min_i == 0 : 
            l = 0 
            r = len(nums)-1 
        elif target >= nums[0] and target <= nums[min_i -1]: 
            l = 0 
            r = min_i -1 
        else : 
            l = min_i 
            r = len(nums)-1 

        # now just a traditional binary search : 

        while l <= r : 
            m = (l+r)//2 

            if nums[m] == target : 
                return m 
            elif nums[m] < target : 
                l = m + 1 
            else : 
                r = m - 1

        return -1
        