class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        text = list(t)
        for i in range(len(s)):
            if len(s)==len(t):
                if s[i] in text:
                    text.pop(text.index(s[i]))
                else:
                    return False
            else:
                return False
        return True