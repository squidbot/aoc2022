movements = {
  'R': (1,0),
  'L': (-1, 0),
  'U': (0, 1),
  'D': (0, -1)
}

def t_sub(a, b): # subtract tuple pairs
  return (a[0] - b[0], a[1] - b[1])

def t_add(a, b): # subtract tuple pairs
  return (a[0] + b[0], a[1] + b[1])

def calc_pos(hp,tp):
  dist = t_sub(hp, tp)
  new_tp = list(tp)
  if dist[0] > 1:
    new_tp[0] += 1
    if dist[1] > 0:
      new_tp[1] += 1
    elif dist[1] < 0:
      new_tp[1] -= 1
  elif dist[0] < -1:
    new_tp[0] -= 1
    if dist[1] > 0:
      new_tp[1] += 1
    elif dist[1] < 0:
      new_tp[1] -= 1
  elif dist[1] > 1:
    new_tp[1] += 1
    if dist[0] > 0:
      new_tp[0] += 1
    elif dist[0] < 0:
      new_tp[0] -= 1
  elif dist[1] < -1:
    new_tp[1] -= 1
    if dist[0] > 0:
      new_tp[0] += 1
    elif dist[0] < 0:
      new_tp[0] -= 1
  return tuple(new_tp)

def part1(lines):
  solution = 0
  visited = set()
  hp = tp = (0,0)
  visited.add(tp)
  for line in lines:
    line = line.strip()
    d, s = line.split(' ')
    s = int (s)
    for step in range(s):
      hp = t_add(hp, movements[d])  # move head
      # determine if tail and head are far enough apart to move tail, then adjust tail
      tp = calc_pos(hp, tp)
      visited.add(tp)
#      print("line:", line, "hp:", hp, "tp:", tp, "dist:", dist)
  solution = len(visited)
  print("solution 1:", solution)  

def part2(lines):
  solution = 0
  visited = set()
  knots = knots = [tuple([0,0]) for x in range(10)]
  HP = 0
  TP = 9
  visited.add(knots[TP])
  for line in lines:
    line = line.strip()
    d, s = line.split(' ')
    s = int (s)
    for step in range(s):
      knots[HP] = t_add(knots[HP], movements[d])  # move head
      # determine if tail and head are far enough apart to move tail, then adjust tail
      for index in range(1,10):
        knots[index] = calc_pos(knots[index - 1], knots[index])
      visited.add(knots[TP])
  solution = len(visited)
  print("solution 2:", solution)  


if __name__ == '__main__':
#  fileName = './input_test.txt'
#  fileName = './input_test_2.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)