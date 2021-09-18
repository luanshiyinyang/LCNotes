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
