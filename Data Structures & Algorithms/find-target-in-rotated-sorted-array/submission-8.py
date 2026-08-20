class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to find minimum number index as that divides the array to 
        # two separate increasing order list 
        
        l = 0 
        r = len(nums)-1

        while l < r : 
            m = (l+r)//2 
            if nums[m] > nums[r]: 
                l = m+1 
            else : 
                r = m 
        

        minimum_index = l 

        # making bounds for a binary search: 
        if minimum_index == 0 : 
            l ,r = 0 , len(nums)-1 
        elif target >= nums[0] and target <= nums[minimum_index -1]: 
            l ,r = 0 , minimum_index - 1 
        else : 
            l = minimum_index 
            r = len(nums)-1

        # binary search for index of target : 
        while l<= r: 
            m = (l+r)//2 
            if nums[m] == target : 
                return m 
            elif nums[m] < target : 
                l = m+1
            else :
                r = m-1
        
        return -1


            
        
        