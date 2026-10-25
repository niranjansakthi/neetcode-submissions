from collections import defaultdict
class Solution:
    def maxDifference(self, s: str) -> int:

        collection = defaultdict(int)

        for char in s:
            collection[char] += 1

        even_freq=[]
        odd_freq =[]

        for chars,freq in collection.items():
            if freq % 2 == 0:
                even_freq.append(freq)
            else:
                odd_freq.append(freq)
            
        max_diff = -float('inf')
        for o in odd_freq:
            for e in even_freq:
                max_diff = max(max_diff,o-e)
        return max_diff


        