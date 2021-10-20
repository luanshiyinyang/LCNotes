const minMoves = (nums: number[]): number => {
  return nums.reduce((pre, cur) => pre + cur) - Math.min(...nums) * nums.length
}
