from copy import deepcopy
from random import sample
from random import choices

solver_1 = __import__('1-naive-solver')

def get_averaege_steps(test_runs=1000, replacement=False, num_colors=5 ):
  total_steps = 0
  for i in range(test_runs):
    COLORS_MAP = {
      5: ["red", "blue", "green", "purple"],
      6: ["red", "blue", "green", "purple", "orange"]
    }
    COLORS = COLORS_MAP.get(num_colors)
    if replacement:
      answer = choices(COLORS, k=4)
    else:
      answer = sample(COLORS, 4)
    board, state = solver_1.solve_master_mind(answer, replacement, num_colors)
    steps = len(board)
    total_steps += steps
  average_steps = total_steps/test_runs
  return average_steps


if __name__ == "__main__":
  test_runs = 1000
  num_colors = [5, 6]
  replacement = [False, True]
  for n in num_colors:
    for r in replacement:
      average_steps = get_averaege_steps(test_runs, r, n)
      print(f'Test for replacement: {r} and num colors: {n}')
      print(f'Average number of steps: {average_steps}')