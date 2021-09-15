class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if s[i] not in stack:
                    while stack[-1] > s[i] and stack[-1] in s[i:]:
                        stack.pop()
                        if not stack:
                            break
                    stack.append(s[i])
        return ''.join(stack[i] for i in range(len(stack)))