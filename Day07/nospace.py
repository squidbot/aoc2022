def build_fs(lines):
  fs = {'/': {}}
  cur = []
  cur.append(fs['/'])
  for line in lines:
    line = line.strip()
    cmd = line.split(' ')
    if cmd[0] == '$':
      #command
      if cmd[1] == 'cd':
        if cmd[2] == '..':
          cur.pop()
        elif cmd[2] == '/':
          cur.clear()
          cur.append(fs['/'])
        else:
          cur.append(cur[-1][cmd[2]])
    elif cmd[0] == 'dir':
      # directory
      cur[-1][cmd[1]] = {}
    else:
      cur[-1][cmd[1]] = int(cmd[0])

  return fs

def find_small(dir, dirname, solution):
  total = 0
  for name in dir:
    if type(dir[name]) is dict:
      prev_total, solution = find_small(dir[name], name, solution)
      total = total + prev_total
    else:
      total = total + dir[name]
  if total <= 100000:
    print("dir:", dirname, "size:", total)
    solution = solution + total
  return total, solution

def get_sizes(dir, sizes):
  total = 0
  for name in dir:
    if type(dir[name]) is dict:
      prev_total = get_sizes(dir[name], sizes)
      total = total + prev_total
    else:
      total = total + dir[name]
  sizes.append(total)
  return total

def part1(fs):
  solution = 0
  total, solution = find_small(fs['/'], '/', solution)  
  print("solution 1:", solution)  

def part2(fs):
  solution = 0
  sizes = []
  get_sizes(fs['/'], sizes)
  sizes.sort()
  print(sizes)
  largest = sizes[-1]
  free_space = 70000000 - largest
  print("free space:", free_space)
  need_to_free = 30000000 - free_space
  print("need to free:", need_to_free)
  for size in sizes:
    if size >= need_to_free:
      print("possible size:", size)
      if solution == 0:
        solution = size
  print("solution 2:", solution)  
    
if __name__ == '__main__':
#  fileName = './input_test.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    fs = build_fs(lines)
    part1(fs)
    part2(fs)