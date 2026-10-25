
from collections import Counter,defaultdict
from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        words = s1.split() + s2.split()
        uniq = defaultdict(int)

        for char in words:
            uniq[char] +=1

        
        return [word for word,freq  in uniq.items() if freq == 1]
        