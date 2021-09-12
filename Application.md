# 加入仓库流程

## 申请

首先需要向仓库管理员，[luanshiyinyan](https://github.com/luanshiyinyang)提出申请，管理员会将你邀请为仓库协作者。

## 格式规范

### 文件组织格式

根目录下的Markdown为笔记内容，`Problems`文件夹存放如下格式的文件，其中题目ID若为主站题库则采用四位数ID如0001，剑指Offer则采用lcof-001这类ID，其他题库采用other-001这类名称。每道题以ID为名为一个子文件夹，其中存放包含`题目描述`、`题解思路`、`优化思路`（可选）等二级标题写成的名为README.md的文件，另一个文件为solv.py存放题解代码。如果题解md文件中需要图片则也放在这个文件夹下即可，后续管理员会手动将其上传图床。

```
└─Problems
    ├─题目ID
       ├─README.md
       ├─solve.py
    ├─题目ID
    └─题目ID
```

### 根目录索引Markdown笔记格式

本仓库目前采用列表式目录进行**题目归档**，**表格式存储**题库，加入的题目建议采用下面的格式。（Markdown书写参考[中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.zh-CN.md)）

首先是题目归档，**这里注意不是所有题目都要进行同一题型的归档，琐碎的题目只需要更新表格式存储即可。** 题目归档的格式如下，其中题目ID要求按照下面表格式存储的要求填写，题目中文名不需自己翻译而是采用力扣中国题库的翻译。

```
### 归档类名

- [题目ID 题目中文名](题目本仓库MD文件索引)
- [题目ID 题目中文名](题目本仓库MD文件索引)
- [题目ID 题目中文名](题目本仓库MD文件索引)
```

举例如下。

```
### 二叉树

- [locf-26 树的子结构](./Problems/lcof-026/README.md)
- [locf-27 二叉树的镜像](./Problems/lcof-027/README.md)
- [locf-28 对称的二叉树](./Problems/lcof-028/README.md)
```

接着是表格存储，这是必须更新的内容，上面的归档是可选的。表格式存储目前分为LeetCode主站题库、力扣中国剑指Offer题库和其他题库（面试真题），其中对主站题库的要求是题目直接输入四位数ID（不足则补0）、题目名称一律采用英文站名称（但是归档时必须采用力扣中国题库题名）、题目类型按照自己的理解填写，包括算法和数据结构两类（如`数组`、`动态规划`等）。对剑指Offer题库和其他题库要求类似，不过ID应当为`剑指Offer 两位数ID`和`Other 两位数ID`，且题目名称为中文。

举例如下。

```
|题目ID|原题链接|题目全名|题目难度|题目类型|题解(<mark>点击下方</mark>)|
|:---:|:--:|:--:|:--:|:--:|:--:|
|21|[link](https://leetcode.com/problems/merge-two-sorted-lists/)|Merge Two Sorted Lists|Easy|数据结构-链表|[link](./Problems/0021/README.md)|

```

## 远程推送要求

Git基础教程和多人写作教程参考下面两篇博客，我们的建议命令如下（**项目根目录进行**）。

- [Git基础教程](https://zhouchen.blog.csdn.net/article/details/107125707)
- [Git协作教程](https://zhouchen.blog.csdn.net/article/details/107294802)

首先你需要进行仓库配置，下面的操作均是已被邀请为协作者才能顺利进行，只需要第一次配置时执行。

```
git clone git@github.com:luanshiyinyang/LCNotes.git
git remote add origin git@github.com:luanshiyinyang/LCNotes.git
git remote add origin-cn git@gitee.com:luanshiyinyang/LCNotes.git
```

下面是平时更新仓库采用的命令，包括拉取仓库最新更新、进行文件修改和增删后更新版本并推送。

```
# 拉取最近的版本
git pull origin main
# 进行本地文件增删
git add .
git commit -m "本次更新题目的描述，如lcof 001"
git push origin main
git push origin-cn main
```