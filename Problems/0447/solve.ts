const numberOfBoomerangs = (points: number[][]): number => {
  const distanceMap = new Map<number, number>()
  let res = 0
  for (const i of points) {
    for (const j of points) {
      const distance = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
      distanceMap.set(distance, ~~distanceMap.get(distance) + 1)
    }
    for (const value of distanceMap.values()) {
      res += value * (value - 1)
    }
    distanceMap.clear()
  }
  return res
}
