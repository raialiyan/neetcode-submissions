class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                for k in range (j+1 ,len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        temp = sorted([nums[i],nums[j],nums[k]])
                        ans.add(tuple(temp))
        for i in ans : 
            res.append(list(i))
        return(res)

        