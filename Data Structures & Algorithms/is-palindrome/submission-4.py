class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        new_string = cleaned[::-1]
        if (cleaned == new_string):
            return True
        else: 
            return False