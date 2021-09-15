class Solution:
    def removeKdigits1(self, num: str, k: int) -> str:
        if k == len(num): return '0'
        res = len(num) - k
        stack = []
        for i in range(len(num)):
            if not stack: 
                stack.append(num[i])
            else:
                if stack[-1] <= num[i] and len(stack) < res:
                    stack.append(num[i])
                if stack[-1] > num[i]:
                    while stack[-1] > num[i] and len(num) - i > res - len(stack):
                        stack.pop()
                        if not stack: break
                    stack.append(num[i])

        for i in range(len(stack)):
            if stack[i] != '0':
                temp = i
                break
        stack = stack[i:]
        return ''.join(stack[i] for i in range(len(stack)))


    def removeKdigits2(self, num: str, k: int) -> str:
        numStack = []
        
        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
        
        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack
        
        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"