import math

def parse(lines):
  monkey_data = []
  cur_monkey_data = None
  for line in lines:
    line = line.strip()
    sp = line.split(' ')
    if len(sp) == 1:
      monkey_data.append(cur_monkey_data)
    elif sp[0] == "Monkey":
      cur_monkey_data = {}
      cur_monkey_data['inspected'] = 0
    elif sp[0] == "Starting":
      items = [int(item.strip(',')) for item in sp[2:]]
      cur_monkey_data['items'] = items
    elif sp[0] == "Operation:":
      cur_monkey_data['operator'] = sp[4]
      cur_monkey_data['operand'] = sp[5]
    elif sp[0] == "Test:":
      cur_monkey_data['test'] = int(sp[3])
    elif sp[1] == "true:":
      cur_monkey_data['true'] = int(sp[5])
    elif sp[1] == "false:":
      cur_monkey_data['false'] = int(sp[5])

  monkey_data.append(cur_monkey_data)

  return monkey_data


def part1(monkey_data):
  solution = 0
  for round in range(20):
    for monkey in monkey_data:
      for item in monkey['items']:
        monkey['inspected'] += 1
        val = item
        if monkey['operand'] == 'old':
          if monkey['operator'] == '+':
            val = val + val
          else:
            val = val * val
        else:
          op = int(monkey['operand'])
          if monkey['operator'] == '+':
            val += op
          else:
            val *= op
        val = math.floor(val / 3)
        if val % monkey['test'] == 0:
          monkey_data[monkey['true']]['items'].append(val)
        else:
          monkey_data[monkey['false']]['items'].append(val)
      monkey['items'].clear()

  inspected = [monkey['inspected'] for monkey in monkey_data]
  inspected.sort(reverse=True)
  solution = inspected[0] * inspected[1]

  print("solution 1:", solution)  

def part2(monkey_data):
  solution = 0
  
  tests = [monkey['test'] for monkey in monkey_data]
  d = math.prod(tests)
  
  for round in range(10000):
    print("Round:", round)
    for monkey in monkey_data:
      for item in monkey['items']:
        monkey['inspected'] += 1
        val = item
        if monkey['operand'] == 'old':
          if monkey['operator'] == '+':
            val = val + val
          else:
            val = val * val
        else:
          op = int(monkey['operand'])
          if monkey['operator'] == '+':
            val += op
          else:
            val *= op
          val = math.floor(val % d)
        if val % monkey['test'] == 0:
          monkey_data[monkey['true']]['items'].append(val)
        else:
          monkey_data[monkey['false']]['items'].append(val)
      monkey['items'].clear()

  inspected = [monkey['inspected'] for monkey in monkey_data]
  inspected.sort(reverse=True)
  solution = inspected[0] * inspected[1]

  print("solution 2:", solution)  
    
if __name__ == '__main__':
#  fileName = './input_test.txt'
  fileName = './input.txt'
  with open(fileName) as f:
    lines = f.readlines()
    monkey_data = parse(lines)
    part1(monkey_data)
    monkey_data = parse(lines)
    part2(monkey_data)