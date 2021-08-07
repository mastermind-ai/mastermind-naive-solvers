from copy import deepcopy
import json

INDEX_COLORS = {
  0: "red",
  1: "blue",
  2: "green",
  3: "purple",
  4: "yellow",
}

COLORS_INDEX = {
  "red": 0,
  "blue": 1 ,
  "green": 2,
  "purple": 3,
  "yellow": 4,
}
answer = ["yellow", "blue", "green", "red"]
guess = ["red", "blue", "green", "purple"]

def unique(list1):
  list_set = set(list1)
  unique_list = (list(list_set))
  return unique_list

def get_move_score(guess, answer):
  correct_color_location, correct_color_wrong_location = 0, 0
  for index, value in enumerate(guess):
    correct_color_location += 1 if value == answer[index] else False
  for value in unique(guess):
    correct_color_wrong_location += 1 if value in answer else False
  correct_color_wrong_location -= correct_color_location
  incorrect = 4 - correct_color_wrong_location - correct_color_location
  return incorrect, correct_color_wrong_location, correct_color_location

def state_to_color(incorrect, semi, perfect):
  return ["default"] * incorrect + ["white"] * semi + ["black"] * perfect

def solve_master_mind(answer):
  # since no repetition, track visited colors
  board, state, visited_colors = [], [], []
  prediction = ["red", "blue", "green", "purple"]
  incorrect, semi, perfect = get_move_score(prediction, answer)
  current_state = state_to_color(incorrect, semi, perfect)
  board.append(prediction)
  state.append(current_state)
  previous_perfect = perfect
  current_slot = 0
  while perfect != 4:
    # vary the colors by slot
    current_color = prediction[current_slot]
    current_color_Index = COLORS_INDEX[current_color]
    new_color_index = current_color_Index + 1
    new_color = INDEX_COLORS[new_color_index%5]
    while new_color in visited_colors:
      new_color_index += 1
      new_color = INDEX_COLORS[new_color_index%5]
    new_prediction = deepcopy(prediction)
    new_prediction[current_slot] = new_color
    # Get the feedback for the new prediction
    [incorrect, semi, perfect] = get_move_score(new_prediction, answer)
    current_state = state_to_color(incorrect, semi, perfect)
    board.append(new_prediction)
    state.append(current_state)
    # Case 1: previous guess was wrong and new guess also wrong
    if perfect == previous_perfect:
      # enables the start of the loop to change color
      prediction = new_prediction
    # Case 2: previous guess for the slot was correct
    elif perfect < previous_perfect:
      visited_colors.append(current_color)
      current_slot += 1
    # Case 3: new guess is correct
    else:
      prediction = new_prediction
      visited_colors.append(new_color)
      current_slot += 1
      previous_perfect = perfect
  return board, state

if __name__ == "__main__":
  board, state = solve_master_mind(answer)
  for index, board_value in enumerate(board):
    print(f'iteration: {index} guess: {board_value} feedback: {state[index]}')