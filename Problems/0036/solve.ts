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
