class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set ()
        i = 0 
        res = 0 
        for j in range(len(s)):
            while s[j] in char_set : 
                char_set.remove(s[i]) # remove the dublicate
                i+=1
            char_set.add(s[j]) 
            length = j - i +1
            res = max(res, length)
        return res