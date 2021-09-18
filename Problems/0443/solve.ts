const compress = (chars: string[]): number => {
  let target: string = chars[0]
  let n: number = 0
  for (let i = 0; i < chars.length; i++) {
    if (chars[i] == target) n++
    else {
      target = chars[i]
      if (n == 1) continue
      chars.splice(i - n + 1, n - 1, ...n.toString())
      i -= n - n.toString().length - 1
      n = 1
    }
  }
  n == 1 || chars.splice(chars.length - n + 1, n - 1, ...n.toString())
  return chars.length
}
