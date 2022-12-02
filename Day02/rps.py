def score():
  with open('./input.txt') as f:
    lines = f.readlines()
    score = 0
    shape_val = {'X':1, 'Y':2, 'Z':3}
    outcome = {
      'A X':3,
      'A Y':6,
      'A Z':0,
      'B X':0,
      'B Y':3,
      'B Z':6,
      'C X':6,
      'C Y':0,
      'C Z':3,
    }
    for line in lines:
      line = line.strip()
      score += outcome[line] + shape_val[line[2]]
    print("score:", score)  

# X LOSE
# Y DRAW
# Z WIN
def score_strat():
  with open('./input.txt') as f:
    lines = f.readlines()
    score = 0
    shape_val = {'X':1, 'Y':2, 'Z':3}
    outcome = {
      'A X':0,
      'A Y':3,
      'A Z':6,
      'B X':0,
      'B Y':3,
      'B Z':6,
      'C X':0,
      'C Y':3,
      'C Z':6,
    }

    outcome_shape = {
      'A X':'Z',
      'A Y':'X',
      'A Z':'Y',
      'B X':'X',
      'B Y':'Y',
      'B Z':'Z',
      'C X':'Y',
      'C Y':'Z',
      'C Z':'X',
    }

    for line in lines:
      line = line.strip()
      score += outcome[line] + shape_val[outcome_shape[line]]
    print("score:", score)  
    

if __name__ == '__main__':
  score()
  score_strat();