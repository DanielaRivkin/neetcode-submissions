class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = { 
            ")": "(",
            "]" : "[", 
             "}" : "{"
        }
        for c in s:
            if c in closedToOpen:
                if not stack or stack[-1] != closedToOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack