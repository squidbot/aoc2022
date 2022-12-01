def most_calories():
  with open('./input.txt') as f:
    lines = f.readlines()
    count = 0
    largest = 0
    for line in lines:
      if line.strip():
        count += int(line)
      else:
        if count > largest:
          largest = count
        count = 0
    if count > largest: #pick up final lines
      largest = count
  print("largest: ", largest)
  
def top_three():
  with open('./input.txt') as f:
    lines = f.readlines()
    count = 0
    totals = []
    for line in lines:
      if line.strip():
        count += int(line)
      else:
        totals.append(count)
        count = 0
    totals.append(count)  #pick up final lines
    totals.sort(reverse=True)
    print("total of top 3: ", sum(totals[0:3]))

if __name__ == '__main__':
  most_calories()
  top_three();