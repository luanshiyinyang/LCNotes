## 题目描述

请你判断一个 9x9 的数独是否有效。只需要 **根据以下规则** ，验证已经填入的数字是否有效即可。

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
4. 数独部分空格内已填入了数字，空白格用 '.' 表示。

**注意：**

* 一个有效的数独（部分已被填充）不一定是可解的。
* 只需要根据以上规则，验证已经填入的数字是否有效即可。

**示例1：**

<img src='./sudoku.png'>

```
输入：board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true
```

**示例2：**

```
输入：board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
```

## 题解思路

本题只需证明数独是否合法，无需证明数独是否可解，因此只要保证题中所给三个条件判断即可。

可以构造三个二维数组对应三个条件，然后遍历数独，若三个数组对应的块存在这个数，就返回 false ，否则将这个数放入三个数组中。时间复杂度为$O(1)$，空间复杂度为$O(1)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
const isValidSudoku = (board: string[][]): boolean => {
  const col: string[][] = Array.from(new Array(9), () => [])
  const row: string[][] = Array.from(new Array(9), () => [])
  const block: string[][] = Array.from(new Array(9), () => [])
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      let num = board[i][j]!
      if (num != '.') {
        if (col[i].includes(num)) return false
        col[i].push(num)
        if (row[j].includes(num)) return false
        row[j].push(num)
        if (block[3 * Math.floor(i / 3) + Math.floor(j / 3)].includes(num)) return false
        block[3 * Math.floor(i / 3) + Math.floor(j / 3)].push(num)
      }
    }
  }
  return true
}

```