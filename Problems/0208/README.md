## 题目描述

Trie（发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

* Trie() 初始化前缀树对象。
* void insert(String word) 向前缀树中插入字符串 word 。
* boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
* boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


**示例**
```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

```

## 题解思路

Trie，又称前缀树或字典树，是一棵有根树。如['apple', 'app', 'aply']可转化为：

<svg width="580" height="400" xmlns="http://www.w3.org/2000/svg">

 <g>
  <title>background</title>
  <rect fill="#fff" id="canvas_background" height="402" width="582" y="-1" x="-1"/>
  <g display="none" overflow="visible" y="0" x="0" height="100%" width="100%" id="canvasGrid">
   <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%" width="100%"/>
  </g>
 </g>
 <g>
  <title>Layer 1</title>
  <ellipse stroke="#000" ry="24.499999" rx="24.999999" id="svg_1" cy="33.953125" cx="277.499999" stroke-width="1.5" fill="#fff"/>
  <ellipse stroke="#000" ry="21.499999" rx="22.499999" id="svg_2" cy="172.953125" cx="279.000001" stroke-width="1.5" fill="#fff"/>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_4" y="42" x="256" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">root</text>
  <line stroke="#000" stroke-linecap="null" stroke-linejoin="null" id="svg_9" y2="78.453127" x2="276.5" y1="57.453129" x1="276.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="none"/>
  <ellipse ry="22" rx="23" id="svg_10" cy="102.453125" cx="276.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="#fff"/>
  <line stroke="#000" stroke-linecap="null" stroke-linejoin="null" id="svg_11" y2="148.453126" x2="277.5" y1="124.453125" x1="275.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="none"/>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_12" y="112.453125" x="269.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">a</text>
  <text transform="rotate(-1.420418381690979 280.179687499998,171.95312499999852) " xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_13" y="180.453125" x="273.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">p</text>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_14" y2="218.453125" x2="240.5" y1="187.453125" x1="259.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_15" y2="216.453125" x2="318.5" y1="184.453125" x1="300.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <ellipse stroke="#000" ry="19" rx="19.5" id="svg_16" cy="237.453125" cx="230" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="#fff"/>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_18" y="245.453125" x="226.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">l</text>
  <ellipse stroke="#000" ry="18.5" rx="19" id="svg_19" cy="296.953125" cx="228.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="#fff"/>
  <ellipse stroke="#000" ry="20.500001" rx="18.5" id="svg_20" cy="349.953124" cx="229" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="#fff"/>
  <ellipse ry="19" rx="22.5" id="svg_21" cy="239.453125" cx="320" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="#fff"/>
  <ellipse ry="22" rx="22" id="svg_22" cy="283.453125" cx="369.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="#fff"/>
  <ellipse stroke="#000" ry="16.5" rx="18" id="svg_23" cy="282.953125" cx="295.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="#fff"/>
  <ellipse stroke="#000" ry="18.000001" rx="18.5" id="svg_24" cy="328.453126" cx="296" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="#fff"/>
  <ellipse stroke="#000" ry="16.5" rx="18" id="svg_25" cy="375.953125" cx="298.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" fill="#fff"/>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_26" y2="263.453125" x2="359.5" y1="246.453125" x1="339.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_27" y2="266.453125" x2="299.5" y1="254.453125" x1="306.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_28" y2="309.453125" x2="295.5" y1="299.453125" x1="295.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_29" y2="359.453125" x2="298.5" y1="346.453125" x1="298.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_30" y2="276.453125" x2="230.5" y1="256.453125" x1="230.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <line stroke-linecap="null" stroke-linejoin="null" id="svg_31" y2="327.453125" x2="230.5" y1="313.453125" x1="228.5" fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000" fill="none"/>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_32" y="240.453125" x="317.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">p</text>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_33" y="290.453125" x="292.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">l</text>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_34" y="333.453125" x="291.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">e</text>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_35" y="302.453125" x="223.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">y</text>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_36" y="356.453125" x="216.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">-1</text>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_37" y="382.453125" x="289.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">-1</text>
  <text xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" id="svg_38" y="293.453125" x="358.5" fill-opacity="null" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#000000">-1</text>
 </g>
</svg>

字典树的节点有两种类型的节点，一种是表示字符串的所有可能字符类型，另一种为判断是否结束的标志。对于本题而言，节点的可能值为26个英文字母和布尔字段 isEnd。

insert 方法的思路是：遍历字符串中的每个字符，如果指针子节点存在值等于该字符，则指针指向该子节点，比较下个字符，如果不存在，则创建一个值为该字符的子节点，指针并指向它，继续比较下个字符。遍历完成后，给当前指针加上 isEnd 的子节点，代表指针为字符串的结尾。

search 方法的思路是：遍历字符串中的每个字符，如果指针子节点存在值等于该字符，则指针指向该子节点，比较下个字符，如果不存在，返回 false。遍历完成后，若指针子节点存在 isEnd 字段，则返回 true，否则返回 false。

startsWith 方法的思路是：遍历字符串中的每个字符，如果指针子节点存在值等于该字符，则指针指向该子节点，比较下个字符，如果不存在，返回 false。遍历完成后，返回 true。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
class Trie {
  children = {}

  constructor() {}

  insert(word: string): void {
    let node = this.children
    for (const character of word) {
      if (!node.hasOwnProperty(character)) node[character] = {}
      node = node[character]
    }
    node['isEnd'] = true
  }

  search(word: string): boolean {
    let node = this.children
    for (const character of word) {
      if (!node.hasOwnProperty(character)) return false
      node = node[character]
    }
    return !!node['isEnd']
  }

  startsWith(prefix: string): boolean {
    let node = this.children
    for (const character of prefix) {
      if (!node.hasOwnProperty(character)) return false
      node = node[character]
    }
    return true
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */


```
