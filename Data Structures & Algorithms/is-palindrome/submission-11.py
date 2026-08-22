class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''

        for c in s : 
            if c.isalnum():                  # this way we are ignoring non alphanumeric characters
                new_string += c.lower()      # conerting to lower case 
        if new_string == new_string[::-1]:   # checking for palindrome 
            return True
        else : 
            return False 

        