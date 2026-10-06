class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buying 
        r = 1 # selling
        max_p = 0 

        while r < len(prices):# iterate right pointer till the end of the list 

            if prices[l] < prices [r]:    # profitable transaction ?
                profit = prices[r] - prices[l]
                max_p = max(max_p , profit)

            else : # price at left pointer was bigger then right pointer
                l = r 
            
            r +=1 # increase the right pointer 

        return max_p 





            

        