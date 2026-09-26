class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens : 
            if c == "+" : 
                stack.append(stack.pop() + stack.pop())

            elif c == "-":
                a , b = stack.pop() , stack.pop()
                stack.append(b - a) # pop() removes things backwards,the most recently added number comes out first.

            elif c == "*" : 
                stack.append(stack.pop() * stack.pop())
            elif c == "/" :
                a , b = stack.pop() , stack.pop()
                stack.append(int(b / a)) # need to convert to integer here as division might lead to float 

            else : 
                stack.append(int(c))

        return stack[0]    

        