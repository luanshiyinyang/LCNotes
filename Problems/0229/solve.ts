const majorityElement = (nums: number[]): number[] => {
  let num1 = 0
  let num2 = 0
  let vote1 = 0
  let vote2 = 0
  let count1 = 0
  let count2 = 0
  const res = []
  for (const num of nums) {
    if (num1 == num) vote1++
    else if (num2 == num) vote2++
    else if (vote1 == 0) {
      num1 = num
      vote1++
    } else if (vote2 == 0) {
      num2 = num
      vote2++
    } else {
      vote1--
      vote2--
    }
  }
  for (const num of nums) {
    if (num == num1) count1++
    else if (num == num2) count2++
  }
  if (count1 > nums.length / 3) res.push(num1)
  if (count2 > nums.length / 3) res.push(num2)
  return res
}
