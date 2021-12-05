# 题目描述
你的任务是计算$a^{b}$对 $1337$ 取模，$a$是一个正整数$b$是一个非常大的正整数且会以数组形式给出。

**示例1：**
```
输入：a = 2, b = [1,0]
输出：1024
```
**示例2：**
```
输入：a = 1, b = [4,3,3,8,5,2]
输出：1
```
# 题解思路
采用秦九韶算法来解题，下面介绍一下秦九韶算法：一般地，一元$n$次多项式的求值需要经过$(n+1)*n/2$次乘法和$n$次加法，而秦九韶算法只需要$n$次乘法和$n$次加法。在人工计算时，一次大大简化了运算过程。
秦九韶算法其实不难，它将一个多项式：
$$
f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0}
$$
写成如下形式：
$$\begin{gathered}
f(x) \\
=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0} \\
=\left(\left(a_{n} x^{n-2}+a_{n-1} x^{n-3}+\cdots a_{3} x+a_{2}\right) x+a_{1}\right) x+a_{0} \\
\vdots \\
\left.=\left(\ldots\left(a_{n} x+a_{n-1}\right) x+a_{n-2}\right) x+\cdots+a_{1}\right) x+a_{0}
\end{gathered}$$
那么对于这一题，套用秦九韶算法，便可得到一下递推公式：
$$\operatorname{superPow}(a, b)= \begin{cases}1, & m=0 \\ \operatorname{superPow}\left(a, b^{\prime}\right)^{10} \cdot a^{b_{m-1}}, & m \geq 1\end{cases}$$
最终代码如下，也可见[solve.py](./solve.py)：
```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1
        for e in b:
            ans = pow(ans, 10, MOD) * pow(a, e, MOD) % MOD
        return ans
```