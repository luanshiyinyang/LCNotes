const plusOne = (digits: number[]): number[] => {
  let n = 1
  for (let i = digits.length - 1; i >= 0 && n != 0; i--) {
    if (digits[i] == 9) digits[i] = 0
    else {
      digits[i]++
      n = 0
    }
  }
  if (n == 1) digits.unshift(1)
  return digits
}
