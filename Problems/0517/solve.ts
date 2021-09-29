const findMinMoves = (machines: number[]): number => {
  let count = 0
  const clothesNum = machines.reduce((pre, cur) => pre + cur)
  if (clothesNum % machines.length) return -1
  const avg = clothesNum / machines.length
  let preSum = 0
  let backSum = clothesNum - machines[0]
  for (let i = 0; i < machines.length; i++) {
    count = Math.max(count, Math.max(i * avg - preSum, 0) + Math.max((machines.length - i - 1) * avg - backSum, 0))
    preSum += machines[i]
    backSum -= machines[i + 1]
  }
  return count
}
