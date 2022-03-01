## 题目描述
给定两个大小分别为`m`和`n`的正序（从小到大）数组`nums1`和`nums2`。请你找出并返回这两个正序数组的中位数。算法的时间复杂度应该为$O(log (m+n))$。

**示例1：**
```
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
```

**示例2：**
```
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```

## 题解思路
由于题目需要$O(log (m+n))$的复杂度，所以合并两个数组并排序的方法就不用思考了。看到“log”复杂度，首先想到的就是二分查找。
首先我们定义$m$和$n$为两个数组的长度，那么当$m+n$是奇数的时候，中位数是第$(m+n)//2$个元素，当$m+n$是偶数时，中位数是第$(m+n)/2$个元素和第$(m+n)/2 +1$个元素的平均值。然后这题便被转为寻找两个有序数组中的第$k$小的数，其中$k$为$(m+n)//2$或$(m+n)//2+1$。

假设数组为A和B，先比较$A[k//2-1]$和$B[k//2-1]$。由于两者的前面分别有$A[0 ... k//2-2]$和$B[0 ... k//2-2]$，一共$k-2$个。也就是说，对于$A[k//2-1]$和$B[k//2-1]$来说，最多也就只有$k-2$个元素比它小，所以它就不是第$k$小的数。因此我们可以归纳出：
- $A[k//2-1]<B[k//2-1]$：$A[k//2-1]$不可能是第$k$个数，即$A[0]$到$A[k//2-1]$可以全部排除。
- $A[k//2-1]>B[k//2-1]$：排除$B[0]$到$B[k//2-1]$。
- $A[k//2-1]=B[k//2-1]$：可以按上述任意一种情况来算，此处按第一种方法来算。

在排除之后的数组上继续二分查找。有一种特殊情况便是$A[k//2-1]$或者$B[k//2-1]$越界，那么我们可以直接选取对应数组的最后一个元素，注意，此时必须**根据具体排除的数字的个数去从$k$中减去**，而不是直接减去$k // 2$。

两种边界情况为：
- 某一个数组为空，说明该数组中所有元素都被排除，直接返回另一个数组中第$k$小的元素。
- $k=1$，说明该排除的数字全部排除，只要返回两个数组当前首元素的最小值即可。

代码如下，也可见[solve.py](solve.py)。
```python
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
```

## 优化思路
上述时间复杂度为$O(log(m+n))$，下述方法的复杂度为$O(log(min(m,n)))$。
我们首先把AB两个数组在$i$和$j$两个地方进行切分。将两个数组的左边放在一起，右边放在一起。目前的左半部分为：$A[0]$,..,$A[i-1]$,$B[0]$,..,$B[j-1]$，右半部分为：$A[i]$,..,$A[m-1]$,$B[j]$,..,$B[n-1]$。

满足以下条件时，我们便能得到答案：

- 当A和B的总长度为偶数时：

  1. 两部分长度相等：$i+j=m-i+n-j$ ，即$j=(m+n)/2 -i$
  2. 左半部分的最大值小于等于右半部分的最小值，那么中位数便是$(max(A[i-1],B[j-1] + min(A[i],B[j])) / 2$
- 当总长度为奇数时：

  1. 左半部分比右半部分大1：$i+j=m-i+n-j+1$，即$j=(m+n+1)/2-i$
  2. 左半部分最大值小于等于右半部分最小值，那么中位数就是左半部分多出来的那个最大值，$max(A[i-1],B[j-1])$

上述两个（1）条件可以合$j=(m+n+1)//2-i$，就算总长度为偶数加1//2后不影响结果。

对于两个（2）条件：$max(A[i-1],B[j-1] <= min(A[i],B[j])$，由于数组是正序的，所以自然就有$A[i-1]<A[i]$和$B[i-1]<B[i]$，那么我们只要保证$A[i-1] <= B[j]$和$B[j-1]<=A[i]$，所以现在题目变成了：

在`[0,m]`中找到$i$，使得$A[i-1]<=B[j]$且$B[j-1]<=A[i]$，其中$j=(m+n+1)//2-i$

这等价于：

在`[0,m]`中找到最大的$i$，使得$A[i-1]<=B[j]$，其中$j=(m+n+1)//2-i$

因为此时的$i$为最大的$i$，也就是说$i+1$不满足$A[i-1]<=B[j]$，也就是说当$i+1=i$时，<=应改为>，即$A[i]>B[j-1]$。找到最大的$i$的方法就采用二分查找，代码如下，也可见[solve.py](solve.py)
。

```python
class Solution:
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
```


