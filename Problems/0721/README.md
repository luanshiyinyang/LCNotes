## 题目描述

给定一个列表 `accounts`，每个元素 `accounts[i]` 是一个字符串列表，其中第一个元素 `accounts[i][0]` 是 *名称 (name)*，其余元素是 **emails** 表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。

合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 **按字符 ASCII 顺序排列** 的邮箱地址。账户本身可以以 **任意顺序** 返回。

**示例1：**
```
输入：accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
输出：[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
解释：
第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。
```

**示例2：**
```
输入：accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
输出：[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
```


## 题解思路

我们首先来分析一下，什么情况下两个账户需要合并呢？当且仅当两个账户至少有一个共同邮箱的时候，因此本题的实质是判断所有的邮箱地址中哪些属于同一人。**这种多个集合的合并我们本能想到了并查集进行求解。**

为了使用并查集，我们需要确定有多少个不同的邮箱地址，并维护一个id来表示这个邮箱，以方便并查集的存储，当然为了最后的输出我们还需要记录每个邮箱的对应名称（name），这可以通过两个字典来实现。

然后，我们使用并查集进行合并操作。由于同一个账户的所有邮箱一定属于同一人，因此遍历每个账户，对账户内的邮箱地址进行合并即可。**注意，并查集中存放的是每个邮箱的id。**

完成了合并后，就知道共有多少个不同的账户了，遍历所有的邮箱地址，对每个邮箱地址通过并查集查询出该邮箱属于哪个账户，这样就你整理出每个合并后的账户包含哪些邮箱地址。

最后，整理出输出的格式即可。

代码如下，也可见于[solve.py](./solve.py)。

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2id, email2name = {}, {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email2id:
                    email2name[email] = name
                    email2id[email] = len(email2id)
        
        uf = UnionFind(len(email2id))
        for account in accounts:
            first_index = email2id[account[1]]
            for other_email in account[2:]:
                uf.union(first_index, email2id[other_email])
        
        index2emails = collections.defaultdict(list)
        for email, index in email2id.items():
            index = uf.find(index)
            index2emails[index].append(email)
        
        res = []
        for emails in index2emails.values():
            res.append([email2name[emails[0]]] + sorted(emails))
        return res
```

上述解法的时间复杂度为$O(nlogn)$，需要遍历所有邮箱地址，在并查集内进行查找和合并操作，对于两个不同的邮箱地址，如果它们的祖先不同则需要进行合并，需要进行 2 次查找和最多 1 次合并。一共需要进行 2n 次查找和最多 n 次合并，因此时间复杂度是 $O(2n \log n)=O(n \log n)$。这里的并查集使用了路径压缩，但是没有使用按秩合并，最坏情况下的时间复杂度是 $O(n \log n)$，平均情况下的时间复杂度依然是 $O(n \alpha (n))$，其中 $\alpha$为阿克曼函数的反函数，$\alpha (n)$ 可以认为是一个很小的常数。
整理出题目要求的返回账户的格式时需要对邮箱地址排序，时间复杂度是 $O(n \log n)$。
其余操作包括遍历所有邮箱地址，在哈希表中记录相应的信息，时间复杂度是 $O(n)$，在渐进意义下 $O(n)$ 小于 $O(n \log n)$。因此总时间复杂度是 $O(n \log n)$。

空间复杂度为$O(n)$，主要取决于哈希表和并查集。
