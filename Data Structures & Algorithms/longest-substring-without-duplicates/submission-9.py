class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        res = 0 
        char_set = set()
        for j in range(len (s)):
            while s[j] in char_set : 
                char_set.remove(s[i])
                i +=1
            char_set.add(s[j])
            res = max(res , j-i+1)
        return res
        