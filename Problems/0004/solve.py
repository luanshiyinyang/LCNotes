class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def Kth(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m: return nums2[index2 + k - 1]
                if index2 == n: return nums1[index1 + k - 1]
                if k == 1: return min(nums1[index1], nums2[index2])

                newindex1 = min(index1 + k // 2 - 1, m - 1)
                newindex2 = min(index2 + k // 2 - 1, n - 1)
                p1, p2 = nums1[newindex1], nums2[newindex2]
                if p1 <= p2:
                    k -= newindex1 - index1 + 1
                    index1 = newindex1 + 1
                else:
                    k -= newindex2 - index2 + 1
                    index2 = newindex2 + 1
        m, n, t = len(nums1), len(nums2), len(nums2) + len(nums1)
        if t % 2 == 1:
            return Kth((t + 1) // 2)
        else:
            return (Kth(t // 2) + Kth(t // 2 + 1)) / 2

    
    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2**40
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        # median1：前一部分的最大值
        # median2：后一部分的最小值
        median1, median2 = 0, 0

        while left <= right:
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1