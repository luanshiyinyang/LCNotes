const findLongestWord = (s: string, dictionary: string[]): string => {
  dictionary.sort((a, b) => a.length - b.length || b.localeCompare(a))
  for (let i = dictionary.length - 1; i >= 0; i--) {
    let m = 0
    let n = 0
    while (m < s.length) {
      if (s[m] == dictionary[i][n]) n++
      if (n == dictionary[i].length) return dictionary[i]
      m++
    }
  }
  return ''
}
