import math
import copy

def parse_data(lines):
  moves = []
  stacks = {}
  readingStacks = True
  for line in lines:
    if readingStacks:
      if len(line.strip()) == 0:
        for stack in stacks.values():
          stack.reverse()
        readingStacks = False
      elif line[1] == '1':
          continue
      else:
        # parse stack
        crates = []
        for i,v in enumerate(line):
          if v not in "[] \n":
            stackIndex = math.floor(i / 4) + 1
            if not stacks.get(stackIndex):
              stacks[stackIndex] = []
            stacks[stackIndex].append(v)
    else:
      tokens = line.split(" ")
      moves.append([int(tokens[1]), int(tokens[3]), int(tokens[5])])
  return moves, stacks

def part1(moves, stacks):
  solution = ''
  for move in moves:
    for times in range(move[0]):
      stacks[move[2]].append(stacks[move[1]].pop())
  for key in sorted(stacks.keys()):
    solution += stacks[key][-1]
  print("solution 1:", solution)  

def part2(moves, stacks):
  solution = ''
  for move in moves:
    stacks[move[2]] += stacks[move[1]][-move[0]:]
    stacks[move[1]] = stacks[move[1]][:-move[0]]
  for key in sorted(stacks.keys()):
    solution += stacks[key][-1]
  print("solution 2:", solution)  
    
if __name__ == '__main__':
#  fileName = './input_test.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    moves, stacks = parse_data(lines)
    part1(moves, copy.deepcopy(stacks))
    part2(moves, copy.deepcopy(stacks))