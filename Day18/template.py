def part1(lines):
  solution = 0
  for line in lines:
    line = line.strip()
  print("solution 1:", solution)  

def part2(lines):
  solution = 0
  for line in lines:
    line = line.strip()
  print("solution 2:", solution)  
    
if __name__ == '__main__':
  fileName = './input_test.txt'
#  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)