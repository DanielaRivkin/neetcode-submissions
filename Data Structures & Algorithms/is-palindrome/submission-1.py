import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return s[::-1].lower() == s.lower()
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        # start = 0
        # end = len(newStr) - 1
        # while start <= end:
        #     if newStr[start] != newStr[end]:
        #         return False
        #     start += 1
        #     end -= 1
        # return True