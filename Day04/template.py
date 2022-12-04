def part1(lines):
  solution = 0
  for line in lines:
    line = line.strip()
    pair1, pair2 = line.split(',')
    p1x, p1y = map(int, pair1.split('-'))
    p2x, p2y = map(int, pair2.split('-'))
    if p1x >= p2x and p1y <= p2y:
      solution += 1
    elif p2x >= p1x and p2y <= p1y:
      solution += 1
  print("solution 1:", solution)  

def part2(lines):
  solution = 0
  for line in lines:
    line = line.strip()
    pair1, pair2 = line.split(',')
    p1x, p1y = map(int, pair1.split('-'))
    p2x, p2y = map(int, pair2.split('-'))
    s1 = set(range(p1x, p1y + 1))
    s2 = set(range(p2x, p2y + 1))
    if s1.intersection(s2):
      solution += 1

  print("solution 1:", solution)  
    
if __name__ == '__main__':
  #fileName = './input_test.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)