## 题目描述

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

**示例1：**

![0011](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)
```
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```

**示例2：**

```
输入：height = [1,1]
输出：1
```

**示例3：**

```
输入：height = [4,3,2,1,4]
输出：16
```

**示例4：**

```
输入：height = [1,2,1]
输出：2
```

## 题解思路

矩形的面积由两个方面决定：

* 矩阵的长度：两条垂直线的距离；
* 矩阵的宽度：两条垂直线其中较短一条的长度。

要获取最大面积，这两者应尽量最大化。不妨从数组两边向中间遍历，用两个指针分别指向数组两边的垂线，若垂线长度较大的指针向中间移动，则所有面积都不可能大于当前的面积，因此，应移动长度较小的指针，比较面积大小，获得较大面积。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```cpp
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int left = 0, right = height.size() - 1, res = 0;
        while (left < right)
        {
            res = max(res, (right - left) * min(height[left], height[right]));
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return res;
    }
};

```
