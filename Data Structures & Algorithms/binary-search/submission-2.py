class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l<=r : 
            mid = (r+l)//2 # mid pointer divides array by 2 each iternation so O(log n)

            if nums[mid] > target: 
                r = mid - 1
            elif nums[mid] < target : 
                l = mid + 1 
            else : 
                return mid
        return -1