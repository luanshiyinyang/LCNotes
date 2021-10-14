const peakIndexInMountainArray = (arr: number[]): number => {
  let start = 0
  let end = arr.length - 1
  let half = Math.ceil(start + (end - start) / 2)
  while (half > 0 && half < arr.length - 1) {
    if (arr[half - 1] < arr[half] && arr[half] > arr[half + 1]) break
    else if (arr[half + 1] > arr[half]) {
      start = half
      half = Math.ceil(start + (end - start) / 2)
    } else if (arr[half - 1] > arr[half]) {
      end = half
      half = Math.ceil(start + (end - start) / 2)
    }
  }
  return half
}
