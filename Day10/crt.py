#Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
#What is the sum of these six signal strengths?

def part1(lines):
  solution = 0
  cycle = 1
  x = 1
  interesting_cycle = 20
  for line in lines:
    line = line.strip()
    sp = line.split(' ')
    val = None
    if sp[0] == 'addx':
      val = int(sp[1])
    if sp[0] == "noop":
      cycle += 1
      if cycle == interesting_cycle and interesting_cycle <= 220:
        solution += cycle * x
        print("noop cycle:", cycle, "x:", x, "str:", cycle * x)
        interesting_cycle += 40
    else:
      cycle += 2
      x += val
      if cycle == interesting_cycle and interesting_cycle <= 220:
        solution += cycle * x
        print("addx  outcycle:", cycle, "x:", x, "str:", cycle * x)
        interesting_cycle += 40
      elif cycle - 1 == interesting_cycle and interesting_cycle <= 220:
        solution += interesting_cycle * (x - val)
        print("addx incycle:", cycle, "x:", x, "cycle recorded:", interesting_cycle, "x recorded:", x- val,"str:", interesting_cycle * (x - val))
        interesting_cycle += 40

  print("solution 1:", solution)  

def print_pixel(cycle, x):
  cycle = cycle % 40
  if cycle == 0:
    print("")

  if cycle in range(x - 1, x + 2):
    print("#", end='')
  else:
    print(".", end='')

def part2(lines):
  solution = 0
  x = 1
  cycle = 0
  for line in lines:
    line = line.strip()
    sp = line.split(' ')
    if sp[0] == 'noop':
      print_pixel(cycle, x)
      cycle += 1
    else:
      val = int(sp[1])
      print_pixel(cycle, x)
      cycle += 1
      print_pixel(cycle, x)
      x += val
      cycle += 1 
 
    
if __name__ == '__main__':
 # fileName = './input_test_2.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)