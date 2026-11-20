class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total = len(grid) * len(grid)
        hs = {}
        for row in grid:
            for s in row:
                if s in hs:
                    hs[s] = hs[s]+1
                else:
                    hs[s] = 1

        count = 0

        unseen = [True] * (len(grid)*len(grid)+ 1)
        repeated = -1

        for i,frq in hs.items():
            unseen[i]=False
            if frq >=2:
                repeated = i
        missing = -1
        for x in range(1,total+1):
            if unseen[x]:
                missing = x
                break
        return [repeated,missing]


        