def part1(lines):
  solution = 0
  trees = []
  for line in lines:
    line = line.strip()
    trees.append([int(i) for i in line])
  
  rows = len(trees)
  cols = len(trees[0])
  cur_max_height = -1
  seen = set()

  # from left
  for y in range(rows):
    cur_max_height = -1
    for x in range(cols):
      if trees[y][x] > cur_max_height:
        cur_max_height = trees[y][x]
        if not (x,y) in seen:
          solution += 1
          seen.add((x,y))

  # from right
  for y in range(rows):
    cur_max_height = -1
    for x in range(cols -1, -1, -1):
      if trees[y][x] > cur_max_height:
        cur_max_height = trees[y][x]
        if not (x,y) in seen:
          solution += 1
          seen.add((x,y))

  # from top
  for x in range(cols):
    cur_max_height = -1
    for y in range(rows):
      if trees[y][x] > cur_max_height:
        cur_max_height = trees[y][x]
        if not (x,y) in seen:
          solution += 1
          seen.add((x,y))

  # from bottom
  for x in range(cols):
    cur_max_height = -1
    for y in range(rows -1, -1, -1):
      if trees[y][x] > cur_max_height:
        cur_max_height = trees[y][x]
        if not (x,y) in seen:
          solution += 1
          seen.add((x,y))

  print("solution 1:", solution)  

def part2(lines):
  solution = 0
  for line in lines:
    line = line.strip()

  trees = []
  for line in lines:
    line = line.strip()
    trees.append([int(i) for i in line])
  
  rows = len(trees)
  cols = len(trees[0])

  for y in range(rows):
    for x in range(cols):
      test_tree = trees[y][x]
      score = 0
      total = 0

      # right
      for right in range(x + 1, cols):
        total += 1
        if trees[y][right] >= test_tree:
          break
      score = total
      
      # left
      total = 0
      for left in range(x - 1, -1, -1):
        total += 1
        if trees[y][left] >= test_tree:
          break
      score *= total

      # up
      total = 0
      for up in range(y - 1, -1, -1):
        total += 1
        if trees[up][x] >= test_tree:
          break
      score *= total

      # down
      total = 0
      for down in range(y + 1, rows):
        total += 1
        if trees[down][x] >= test_tree:
          break
      score *= total

      if score > solution:
        solution = score
  print("solution 2:", solution)  
    
if __name__ == '__main__':
#  fileName = './input_test.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)