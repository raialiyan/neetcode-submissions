class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = []
        for i in nums :
            if (i in newlist) :
                return True 
            else: 
                newlist.append(i)
        return False 

        