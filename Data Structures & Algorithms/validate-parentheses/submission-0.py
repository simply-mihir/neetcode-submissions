class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        co = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in co:
                if stack and stack[-1]==co[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False