class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = len(nums)
        for i in range (index) :
            for j in range (i+1,index):
                if (nums[i] + nums[j] == target and i != j):
                    return [i,j]
