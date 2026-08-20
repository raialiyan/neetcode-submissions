class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        new_str = cleaned[::-1]
        if new_str == cleaned : 
            return True
        else: 
            return False