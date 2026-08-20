class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(" , "]":"[" , "}": "{"}
        stack = []

        for c in s : 
            if c not in hashmap : # it will check keys in hashmap so if not in there the c is opening bracket 
                stack.append(c) # we append opening bracket in stack 
            else :             #if its closing bracket 
                if not stack :  # if stack is empty return false
                    return False 
                else:   # othervise the closing bracket should match opening bracket 
                    popped = stack.pop()
                    if popped!= hashmap[c] :
                        return False
        return not stack

     
        