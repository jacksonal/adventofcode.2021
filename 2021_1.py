from util import getLinesFromFile
increaseCount = 0
previousVal = None
lines = list(map(int, getLinesFromFile('./input.txt')))

for val in lines:
  if previousVal is None:
    previousVal = val
    continue
  if val > previousVal:
    increaseCount += 1
  previousVal = val

print(increaseCount)

def getWindowSum(index, iterable):
  if len(iterable) > index + 2:
    return iterable[index] + iterable[index + 1] + iterable[index + 2]
  else:
    return None

increaseCount = 0
previousVal = None

for idx in range(len(lines)):
  val = getWindowSum(idx,lines)
  if val is None:
    break
  if previousVal is None:
    previousVal = val
    continue
  if val > previousVal:
    increaseCount += 1
  previousVal = val

print(increaseCount)