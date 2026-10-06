class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        longest = 0 
        char_set = set () # using set to check for duplicates 
        n = len(s)

        for r in range(n): #using range() cause we want to use index
        

        # when invalid move l when valid move r

            while s[r] in char_set : # while value at right pointer is already in set (invalid)
                char_set.remove(s[l])
                l +=1
                
                   
            #valid now: 
            window_len = (r-l)+1
            longest = max(longest, window_len)
            char_set.add(s[r])

        return longest 

                    