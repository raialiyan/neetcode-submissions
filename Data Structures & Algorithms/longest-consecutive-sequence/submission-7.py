class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        length = len(nums)
        if length == 0 : 
            return 0 
        
        new_set = sorted(set(nums)) 

        streak = 1
        longest = 1

        for i in range(1 , len(new_set)): 
            if (new_set[i] == new_set[i-1]+1):
                streak += 1
                longest = max(longest , streak)
            else :
                streak = 1
        return longest  
