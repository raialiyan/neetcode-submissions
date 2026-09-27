class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        result = [0]*n  # initialize the result array with zeros 

        stack = []

        for i , t in enumerate(temperatures):    # it means i is the index and t is the value in temperatures 
            while stack and stack[-1][0] < t : # if value at the top of the stack is less than the temperature (we got a warmer day)
                stack_t , stack_i = stack.pop() # pop the index and temperature off the stack 
                result[stack_i] = i - stack_i # calculating the day differnce 

            stack.append((t , i)) # if the temp is not warmer than the one on top of stack just append it on the stack 

        return result 



