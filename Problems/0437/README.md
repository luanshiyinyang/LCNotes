## 题目描述
给定一个二叉树的根节点`root`，和一个整数`targetSum`，求该二叉树里节点值之和等于`targetSum`的路径的数目。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

## 题解思路
首先最暴力的方法便是两层递归，第一层递归是遍历买一个结点，第二层递归是找到所以以该结点为根节点的树中路径和为`targetSum`的数量。代码如下，也可见[solve.cpp](solve.cpp)。
```cpp
class Solution {
public:
    int dfs1(TreeNode* root, int target){
        if (!root){
            return 0;
        }
        int ret = 0;
        if (root->val == target){
            ret++;
        }
        ret += dfs1(root->left, target - root->val);
        ret += dfs1(root->right, target - root->val);
        return ret;
    }

    int pathSum1(TreeNode* root, int targetSum) {
        if (!root){
            return 0;
        }
        int ret = dfs1(root, targetSum);
        ret += pathSum1(root->left, targetSum);
        ret += pathSum1(root->right, targetSum);
        return ret;
    }
}
```

## 优化思路
上述暴力递归在leetcode中是会TLE的，所以我们得降低他的时间复杂度。不难发现，上述解法中存在着很多的重复计算，就比如现在有：root->p1->p2->p3->p4，这条路径。在上述方法中，如果要计算p2->p3->p4这条路径，就得以p2为根节点进行递归。然而我们可以记录下每一个节点的前缀和（从root结点到当前节点的路径和），那么p2->p3->p4的路径长度便为p4的前缀和减去p2的前缀和。

那么我们怎么寻找路径长度为`targetSum`的路径呢，当遍历到当前节点的时候（设当前前缀和为`cur`），我们可以搜寻以及记录的前缀和中，是否等于`cur - targetSum`的数量，这边是我们要寻找的。这样以来，我们只需一层递归遍历树的每一个结点即可。
代码如下，也可见[solve.cpp](solve.cpp)。

```cpp
class Solution {
public:
    unordered_map<long long, int> prefix; //key为路径长度，value为路径数量；

    int dfs2(TreeNode* root, long long cur, int targetSum){
        if (!root){
            return 0;
        }
        int ret = 0;
        cur += root->val;
        if (prefix.count(cur - targetSum)){ //找寻前缀和为cur - targeSum的路径的数量；
            ret += prefix[cur - targetSum];
        }
        prefix[cur]++; //记录前缀和为cur的路径加1；
        ret += dfs2(root->left, cur, targetSum);
        ret += dfs2(root->right, cur, targetSum);
        prefix[cur]--; //回溯，退出当前子树后，需要删除。
        return ret;
    }

    int pathSum2(TreeNode* root, int targetSum) {
        prefix[0] = 1;
        int ret = dfs2(root, 0, targetSum);
        return ret;
    }
};
```
