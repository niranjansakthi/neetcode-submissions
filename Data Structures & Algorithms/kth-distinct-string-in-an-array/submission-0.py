class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hs = {}
        for s in arr:
            if s in hs:
                hs[s] +=1
            else:
                hs[s] = 1
           
        count = 0
        for i in arr:
            if hs[i] == 1:
                count+=1
                if count == k:
                    return i
                
        return ""
        
        