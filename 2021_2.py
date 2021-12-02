from os import stat
from util import getLinesFromFile
from functools import reduce


def navigate1(state, instruction):
  lateral = 0
  depth = 0
  split_instr = instruction.split()
  op,distance = split_instr[0], split_instr[1]
  distance = int(distance)
  print(state)
  if op == 'forward':
    lateral = distance
  elif op == 'down':
    depth = distance
  elif op == 'up':
    depth = 0 - distance
  
  return (state[0] + lateral, state[1] + depth)

def navigate2(state,instruction):
  deltaim = 0
  deltdepth = 0
  deltlat = 0
  split_instr = instruction.split()
  op,distance = split_instr[0], int(split_instr[1])

  if op == 'forward':
    deltlat = distance
    deltdepth = distance * state[2]
  elif op == 'down':
    deltaim = distance
  elif op == 'up':
    deltaim = 0 - distance

  return (state[0] + deltlat, state[1] + deltdepth, state[2] + deltaim)

#subState = reduce(navigate1, getLinesFromFile('./input.txt'), (0,0))
subState = reduce(navigate2, getLinesFromFile('./input.txt'), (0,0,0))
print(subState)