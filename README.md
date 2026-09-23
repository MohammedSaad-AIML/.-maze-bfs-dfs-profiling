# SLE-2: BFS vs DFS Maze Profiling

**Course:** 02AML204 — Introduction to Artificial Intelligence  
**PRN:** 25UAM101  
**Name:** MohammedSaad Bijapure  
**Division:** B  
**Date:** 22 September 2026

## Overview

This project profiles and compares two graph-search algorithms:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS), depth-limited to 400**

The algorithms solve a randomly generated **perfect maze** from the top-left start cell to the bottom-right goal cell.

A perfect maze has a single unique path between any two cells. The project measures:

- Execution time
- Number of nodes expanded
- Solution path length
- Runtime behavior using a `py-spy` flame graph

## Project Structure

```text
SLE2_GitHub_Repository/
├── README.md
├── CONTRIBUTION_LOG.md
├── maze_profiling.py
└── profile_driver.py
```

## Requirements

- Python 3.9+
- `matplotlib` (for the comparison chart)
- `py-spy` (for sampling profiling / flame graph)

Install the Python dependency:

```bash
pip install matplotlib
```

Install `py-spy`:

```bash
pip install py-spy
```

## Run the Experiment

Run the main experiment:

```bash
python maze_profiling.py
```

The program:

1. Generates perfect mazes.
2. Runs BFS and depth-limited DFS.
3. Measures each run using `time.perf_counter()`.
4. Counts expanded nodes.
5. Reports path lengths and average timings.
6. Saves the collected results to `results.json`.
7. Creates a comparison chart.

The experiment uses the three maze sizes described in the report:

- `10 x 10`
- `18 x 18`
- `26 x 26`

Five runs are performed for each algorithm/test case.

## Generate a py-spy Flame Graph

Run the profiling driver under `py-spy`:

```bash
py-spy record --rate 100 --duration 3 --output flame.svg -- python profile_driver.py
```

The flame graph shows where the program spends wall-clock sampling time. Wider frames indicate functions that occupy more sampled execution time.

## Reported Results

The submitted profiling report records the following measurements:

| Test case | Algorithm | Avg. time (ms) | Nodes expanded | Path length |
|---|---|---:|---:|---:|
| 10x10 | BFS | 0.0720 | 39 | 32 |
| 10x10 | DFS | 0.0993 | 44 | 32 |
| 18x18 | BFS | 0.1989 | 117 | 100 |
| 18x18 | DFS | 0.7283 | 190 | 100 |
| 26x26 | BFS | 0.5616 | 349 | 190 |
| 26x26 | DFS | 4.3170 | 674 | 190 |

The report notes that, for these perfect mazes, BFS and DFS found the same path lengths because there is only one route between the start and goal. The main difference appeared in execution time and nodes expanded.

## Algorithm Notes

### BFS

BFS explores the maze level-by-level using a queue. For an unweighted graph, BFS can find a shortest path.

### DFS

DFS follows one branch deeply before backtracking. In this project it is depth-limited to 400. Its performance depends strongly on neighbour order and the number of dead ends explored before reaching the goal.

## Profiling Tools

The project uses:

- `time.perf_counter()` for per-run timing
- A manual node counter inside BFS and DFS
- `py-spy` for sampling profiling and flame graphs

`py-spy` is used for understanding where runtime is spent, while `perf_counter()` is used for the small exact timing measurements.

## AI Contribution

According to the SLE-2 report, AI tools were used to help write the maze generator, BFS/DFS solver, profiling driver, figures, and report draft. The student selected the BFS/DFS comparison, selected the maze sizes, reviewed and reran the generated code, checked the results, and wrote the justification based on the measured data.

## Key Takeaway

The experiment demonstrates how the choice of search strategy can affect runtime and the number of explored states even when the final solution path is the same.
