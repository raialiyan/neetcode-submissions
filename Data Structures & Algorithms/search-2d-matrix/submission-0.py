class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix) # number of coloums 
        n = len(matrix[0]) # number of rows , by counting the number of elements in first row

        t = m*n # total elemnets 

        l = 0 
        r = t-1 

        while l <= r : 
            M = (l+r)//2 # middle pointer index
            i = M // n # calculating row and coloum index by using middle pointer
            j = M % n 

            middle_value = matrix [i][j]

            if target == middle_value : 
                return True 

            elif target < middle_value : 
                r = M -1 
            else : 
                l = M +1
        
        return False




        