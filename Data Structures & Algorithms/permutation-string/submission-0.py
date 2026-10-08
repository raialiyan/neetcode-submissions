class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2 : # if n2 is smaller then n1 it cant contain the permutation of n1 
            return False


        # make arrays initialized by zeros
        s1_counts = [0]*26
        s2_counts = [0]*26

        for i in range(n1):
            s1_counts[ord(s1[i]) - 97 ] += 1 # change the value of s1_counts array with ascii value of that letter
            s2_counts[ord(s2[i]) - 97 ] += 1 # change the value of s2_counts array with ascii value of that letter
        
        if s1_counts == s2_counts : # if both arrays have 1s in same position 
            return True 

        for i in range(n1 , n2):                 # for sliding the window in  s2 counts
            s2_counts[ord(s2[i]) - 97] +=1       # adding letter in window 
            s2_counts[ord(s2[i - n1]) - 97] -= 1 # removing from the window 
            if s1_counts == s2_counts : 
                return True

        return False  



        