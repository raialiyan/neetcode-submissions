from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def k_works(k):
            hours = 0 
            for p in piles :             # basically calculating how many hours does each k need and return true if it
                                         # is less than the h we were given 
                hours += ceil(p/k)
            return hours <= h 
        

        l = 1 
        r = max(piles) # r is maximum number of elemnets in piles 

        # Binary search : 

        while l < r :       # here we are using < not <= as the loop will never end then
            k = (l+r)//2

            if k_works(k): 
                r = k      # we might be able to find an even smaller k 
            else : 
                l = k +1 
        
        return r 

                  
    


        

        