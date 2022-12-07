def part1(runIndex, signal):
  solution = 0
  quads = [signal[i:i+4] for i in range(len(signal)-3)]
  for index, quad in enumerate(quads):
    if len(set(quad)) == len(quad):
      solution = index + 4
      break
  print("runIndex:", runIndex, "solution 1:", solution)  

def part2(index, signal):
  solution = 0
  quads = [signal[i:i+14] for i in range(len(signal)-13)]
  for index, quad in enumerate(quads):
    if len(set(quad)) == len(quad):
      solution = index + 14
      break
  print("index: ", index, "solution 2:", solution)  
    
if __name__ == '__main__':
  signals = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',  # 7
    'bvwbjplbgvbhsrlpgdmjqwftvncz',    # 5
    'nppdvjthqldpwncqszvftbrmjlhg',    # 6
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', # 10
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',  # 11
  ]
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    lines[0].strip()
    signals.append(lines[0])
    
    for runIndex, signal in enumerate(signals):
      part1(runIndex, signal)
      part2(runIndex, signal)