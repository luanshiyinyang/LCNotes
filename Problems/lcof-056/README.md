## 题目描述（1）
一个整型数组`nums`里除一个数字之外，其他数字都出现了两次。请写程序找出这个只出现一次的数字。

## 题解思路（1）
这里的三条题目其实都可以采用哈希表的方法写出来，但这里都采用异或的方法。相同的两个数的二进制进行异或操作，是等于0的，比如：
19：1 0 0 1 1
19 ^ 19 = 0 0 0 0 0
那么，数组中所有的数依次进行异或操作，最后的结果便是值出现了一次的数，因为0与任意的数进行异或，结果依旧是它（0 ^ x = x）。


## 题目描述（2）
一个整型数组`nums`里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是$O(n)$，空间复杂度是$O(1)$。

## 题解思路（2）
这题和第一题基本类似，要是我们能将这两个只出现一次的数字分开，分成两个数组，每个数组中有一个数字只出现一次，其他数字出现两次，然后对每一组进行如题目一的解法。所以如何分组很重要。

首先，我们将所有数进行异或操作，最后的结果应该是`a ^ b`，其中`a`和`b`为只出现一次的两个数字。那么，`a ^ b`中为“1”的位置便是`a`和`b`不同的地方，比如：a = 10100，b = 10110，那么`a ^ b`便是00010。我们可以用异或结果中的任意一个位置的“1”来将数组中的数进行分组，这样`a`和`b`便会被分开。然后再像题目1中那样找到`a`和`b`。
代码如下，也可见[solve.py](solve.py)。
```python
class Solution2:
    def singleNumbers(self, nums: list[int]) -> list[int]:
        ret = functools.reduce(lambda x, y : x ^ y, nums) # 将nums中的每一个元素都进行异或操作：a ^ b ^ c ^ ... 
        div = 1
        while div & ret == 0:
            div <<= 1 # 这里找的是最右边一个“1”，任意一个“1”都行
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
```

## 题目描述（3）
在一个数组`nums`中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

**示例：**
```
输入：nums = [9,1,7,9,7,9,7]
输出：1
```

## 题解思路（3）
这题便不能采用异或的方法。但出现三次，我们可以观察到以下规律，比如：

3 = 0 0 1 1

3 = 0 0 1 1

3 = 0 0 1 1

5 = 0 1 0 1

我们统计各个位置上“1”出现的次数，为[0， 1， 3， 4]，再将次数取余3，便会得到[0, 1, 0, 1]，便是我们要找的5。

所以这题的思路便是，统计各个位置上出现“1”的次数再取余3。各二进制位的**位运算规则相同**，因此只需考虑一位即可。对于每个位置上的数字取余3，只存在“0，1，2”三种状态。当下一个二进制位为“1”时，会发生0-1-2-0-1-2...的变化，当下一个二进制位为“0”的时候，状态不变。

由于有三个状态，便要用两位数来代表状态，我们假设状态分别为“00，01，10”。两个位置记作“pq”，输入的数字为“n”。

对于“n”位来说，有
```
if p == 0:
  if n == 0:
    q = q
  if n == 1:
    q = ~q
if p == 1:
    q = 0
```
加入异或运算，可以化简为：
```
if p == 0:
  q = q ^ n
if p == 1:
  q = 0
```
加入或运算，可以化简为：$q = q ^ n & ~p$。
同理可推出，$p = p ^ n & ~q$（此时的q为更新后的q）。
那么，整个代码如下，也可见[solve.py](solve.py)。
```python
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        q, p = 0, 0
        for num in nums:
            q = q ^ num & ~p
            p = p ^ num & ~q
        return q # q位置为1的，只有代表取余3余1的那个状态，所以q便是答案
```