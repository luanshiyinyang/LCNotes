class Solution:
    def minInsertions(self, s: str) -> int:
        l_count, index,  insert = 0, 0, 0
        length = len(s)
        while index < length:
            if s[index] == '(':
                l_count += 1
                index += 1
            else:
                if l_count > 0:
                    l_count -= 1
                else:
                    insert += 1
                if index < length - 1 and s[index+1] == ')':
                    index += 2
                else:
                    insert += 1
                    index += 1
        insert += 2 * l_count
        return insert