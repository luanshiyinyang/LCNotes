class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def find_max_subseqence(n:List[int], k:int):
            if k == 0: return []
            stack = []
            for i in range(len(n)):
                if not stack:
                    stack.append(n[i])
                else:
                    if stack[-1] >= n[i] and len(stack) < k:
                        stack.append(n[i])
                    if stack[-1] < n[i]:
                        while stack[-1] < n[i] and len(n) - i > k - len(stack):
                            stack.pop()
                            if not stack:
                                break
                        stack.append(n[i])
            return stack
        
        def compare(subsequence1: List[int], index1: int, subsequence2: List[int], index2: int) -> int:
            x, y = len(subsequence1), len(subsequence2)
            while index1 < x and index2 < y:
                difference = subsequence1[index1] - subsequence2[index2]
                if difference != 0:
                    return difference
                index1 += 1
                index2 += 1
            return (x - index1) - (y - index2)

        def merge(subsequence1: List[int], subsequence2: List[int]) -> List[int]:
            x, y = len(subsequence1), len(subsequence2)
            if x == 0:
                return subsequence2
            if y == 0:
                return subsequence1
        
            mergeLength = x + y
            merged = list()
            index1 = index2 = 0

            for _ in range(mergeLength):
                if compare(subsequence1, index1, subsequence2, index2) > 0:
                    merged.append(subsequence1[index1])
                    index1 += 1
                else:
                    merged.append(subsequence2[index2])
                    index2 += 1
        
            return merged
        
        ans = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                sub1 = find_max_subseqence(nums1, i)
                sub2 = find_max_subseqence(nums2, k - i)
                maxnum = merge(sub1, sub2)
                print(maxnum)
                if compare(maxnum, 0, ans, 0) > 0:
                    ans = maxnum

        return ans