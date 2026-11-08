class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        take = True
        for i,row in enumerate(grid):
            cols = row if i%2==0 else row[::-1]
            for val in cols:
                if take:
                    res.append(val)
                take = not take

        return res            

                