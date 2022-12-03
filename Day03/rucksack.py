def calculate_priority(item):
    if item.isupper():
      return ord(item) - ord('A') + 27
    else:
      return ord(item) - ord('a') + 1


def part1(lines):
  solution = 0
  for line in lines:
    line = line.strip()
    compartment_size = int(len(line) / 2);
    c1 = set(line[:compartment_size])
    c2 = set(line[compartment_size:])
    common = ''.join(c1.intersection(c2))
    print("common = ", common)
    priority = calculate_priority(common)
    print("priority = ", priority)
    solution += priority

  print("solution 1:", solution)  

def part2(lines):
  solution = 0
  group = []
  for line in lines:
    line = line.strip()
    group.append(line)
    if len(group) == 3:
      common = ''.join(set(group[0]).intersection(set(group[1]).intersection(set(group[2]))))
      print("common = ", common)
      priority = calculate_priority(common)
      print("priority = ", priority)
      solution += priority
      group.clear()
  print("solution 2:", solution)  
    
if __name__ == '__main__':
#  fileName = './input_test.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)