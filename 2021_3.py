from util import getLinesFromFile
from functools import reduce

def countBits(state, num):
  zipped = zip(state,map(int,num))
  return tuple(map(lambda zlist: reduce(lambda x,y:x+y,zlist,0),zipped)) #treat each value as a bitmask and accumulate all 1s

input = getLinesFromFile('./input.txt')
lineCount = len(input)

bitCount = reduce(countBits, input, [0] * len(input[0]))
gamma = int(''.join(map(lambda x: '1' if x > lineCount/2 else '0',bitCount)),2)
epsilon = int(''.join(map(lambda x: '0' if x > lineCount/2 else '1',bitCount)),2)

print(gamma, epsilon, gamma*epsilon)

def findO2rating(values, bitPos):
  valCount = len(values)
  if valCount == 1:
    return values[0]
  else:
    bitCount = list(reduce(countBits, values, [0] * len(values[0])))[bitPos] #find bit frequency for remaining values
    correctBit = '1' if bitCount >= valCount/2 else '0'
    #filter out values 
    return findO2rating(list(filter(lambda x: x[bitPos] == correctBit,values)),bitPos + 1)

def findCO2rating(values, bitPos):
  valCount = len(values)
  if valCount == 1:
    return values[0]
  else:
    bitCount = list(reduce(countBits, values, [0] * len(values[0])))[bitPos] #find bit frequency for remaining values
    correctBit = '0' if bitCount >= valCount/2 else '1'
    #filter out values 
    return findCO2rating(list(filter(lambda x: x[bitPos] == correctBit,values)),bitPos + 1)
    
o2rating = int(findO2rating(input,0),2)
co2rating = int(findCO2rating(input,0),2)
print(o2rating,co2rating,o2rating*co2rating)