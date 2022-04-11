#include <unordered_map>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

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
    
    unordered_map<long long, int> prefix;

    int dfs2(TreeNode* root, long long cur, int targetSum){
        if (!root){
            return 0;
        }
        int ret = 0;
        cur += root->val;
        if (prefix.count(cur - targetSum)){
            ret += prefix[cur - targetSum];
        }
        prefix[cur]++;
        ret += dfs2(root->left, cur, targetSum);
        ret += dfs2(root->right, cur, targetSum);
        prefix[cur]--;
        return ret;
    }

    int pathSum2(TreeNode* root, int targetSum) {
        prefix[0] = 1;
        int ret = dfs2(root, 0, targetSum);
        return ret;
    }
};