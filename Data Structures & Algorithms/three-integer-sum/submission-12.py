class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sorting the numbers
        nums.sort()

        res = []

        # i = first number (fixing it temporaraily and using two other variables as two pointers)
        for i in range(len(nums)):

            # Don't use the same first number again
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # j and k are our two pointers
            j = i + 1
            k = len(nums) - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]

                # Sum too small
                if total < 0:
                    j += 1

                # Sum too big
                elif total > 0:
                    k -= 1

                # Found 0!
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res