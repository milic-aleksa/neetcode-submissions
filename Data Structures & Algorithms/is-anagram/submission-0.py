class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strOne = {}
        strTwo = {}

        if len(s) == len(t):
            for char in s:
                if char in strOne:
                    strOne[char]= strOne.get(char) + 1
                else:    
                    strOne[char] = 1
            for char in t:    
                if char in strTwo:
                    strTwo[char] = strTwo.get(char) + 1
                else:    
                    strTwo[char] = 1

            if strOne == strTwo:
                return True

        return False    
                    