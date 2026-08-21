class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range (9): 
            for c in range(9) : 
                value = board[r][c]
                if value != ("."):
                    if (value in row[r] or 
                        value in col[c] or  
                        value in box[(r // 3 , c // 3) ]) :
                        return False 
                    else : 
                        row[r].add(value)
                        col[c].add(value)
                        box[(r // 3 , c // 3)].add(value)
        return True



        