class Solution:
    def constructArr(self, a: list[int]) -> list[int]:
        b, temp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            temp *= a[i + 1]
            b[i] *= temp
        return b