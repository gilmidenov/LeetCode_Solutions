class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        base = {
            "}":'{',
            ")":'(',
            "]":'[',
        }
        for c in s:
            if c in base:
                top = stack.pop() if stack else "#"
                if base[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack
