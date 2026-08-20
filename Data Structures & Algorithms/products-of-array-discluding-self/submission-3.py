class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [] 
        length = len(nums)
        for i in range (length):
            product = 1 
            for j in range (length): 
                if i != j : 
                    product *= nums[j]
            res.append(product)
        return res
            
        