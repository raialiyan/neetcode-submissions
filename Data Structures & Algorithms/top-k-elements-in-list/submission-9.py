class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        sort_nums = sorted(count , key= count.get , reverse = True)

        return sort_nums[:k]
        