# Naive solvers for Mastermind

## Naive solver 1: Solves using only the feedback from correct color and location

**Run the solver for one case:**

```bash
python 1-naive-solver.py
```

**Solver logic:**

1. Start with a fixed guess
3. For each slot, vary the color till the selection is the correct color
4. Stop the iteration when all the slots are the correct color

**Example**

Target: `['purple', 'red', 'blue', 'green']`

For feedback, the colors represent the following scenarios

- `default`: wrong color, wrong location
- `white`: correct color, wrong location
- `black`: correct color, correct location

| Iteration | Guess                                   | Feedback                                 |
| --------- | --------------------------------------- | ---------------------------------------- |
| 0         | ['red', 'blue', 'green', 'purple']      | ['white', 'white', 'white', 'white']     |
| 1         | ['blue', 'blue', 'green', 'purple']     | ['default', 'white', 'white', 'white']   |
| 2         | ['green', 'blue', 'green', 'purple']    | ['default', 'white', 'white', 'white']   |
| 3         | ['purple', 'blue', 'green', 'purple']   | ['default', 'white', 'white', 'black']   |
| 4         | ['purple', 'green', 'green', 'purple']  | ['default', 'default', 'white', 'black'] |
| 5         | ['purple', 'yellow', 'green', 'purple'] | ['default', 'default', 'white', 'black'] |
| 6         | ['purple', 'red', 'green', 'purple']    | ['default', 'white', 'black', 'black']   |
| 7         | ['purple', 'red', 'yellow', 'purple']   | ['default', 'default', 'black', 'black'] |
| 8         | ['purple', 'red', 'blue', 'purple']     | ['default', 'black', 'black', 'black']   |
| 9         | ['purple', 'red', 'blue', 'yellow']     | ['default', 'black', 'black', 'black']   |
| 10        | ['purple', 'red', 'blue', 'green']      | ['black', 'black', 'black', 'black']     |

