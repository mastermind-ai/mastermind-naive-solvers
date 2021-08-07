# Naive solvers for Mastermind

## Naive solver 1: Solves using only the feedback from correct color and location

**Run the solver for one case:**

```bash
python 1-naive-solver.py
```

- By default this runs with 5 colors and no replacement in the answer
- To adjust this, go to the `1-naive-solver.py` file and change the values assigned to `num_colors` and `replacement` in `if __name__ == "__main__":`

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

**Solver performance**

Run the following to evaluate the algorithm's performance on 1000 solves

```bash
python solver-performance.py
```

Results

| Color configuration | Allow Duplicates? | Average guesses (out of 1000) |
| ------------------- | ----------------- | ----------------------------- |
| 6 choose 4          | No                | 9.469                         |
| 6 choose 4          | Yes               | 11.623                        |
| 5 choose 4          | No                | 7.668                         |
| 5 choose 4          | Yes               | 9.597                         |
