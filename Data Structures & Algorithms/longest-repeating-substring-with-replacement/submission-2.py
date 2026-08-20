class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''All we are doing is making a valid window using two pointers  and taking its length and then returning the longest length '''
        longest = 0 
        l = 0 
        counts = [0]*26

        for r in range(len(s)):
            counts[ord(s[r])-65]+=1 # increase the counts of letter at right pointer
            '''for window to be not valid length of window - max frequency of letter is greater than k i.e number of letters we can replace '''
            while (r-l+1) - max(counts)> k : # if window not valid move left pointer forward and decrease its count 
                counts[ord(s[l])-65]-=1
                l+=1
            longest = max(longest , r - l +1 )
        return longest 


                


        