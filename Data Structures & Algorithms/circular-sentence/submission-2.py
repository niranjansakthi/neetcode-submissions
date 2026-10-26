class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word = sentence.split()
        output = True
        for right in range(0,len(word)):
            if word[right][-1] != word[(right + 1) % len(word)][0]:
                return False
            
        return True

