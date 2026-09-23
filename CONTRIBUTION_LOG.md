# Contribution Log

## Project: SLE-2 — BFS vs DFS Maze Profiling

**Student:** MohammedSaad Bijapure  
**PRN:** 25UAM101  
**Division:** B  
**Course:** 02AML204 — Introduction to Artificial Intelligence

| Contribution | Description | Status |
|---|---|---|
| Problem selection | Selected maze traversal as the search problem. | Completed |
| Algorithm selection | Selected BFS and depth-limited DFS for comparison. | Completed |
| Maze generation | Used a randomly generated perfect maze concept with a unique path between cells. | Completed |
| BFS implementation | Implemented BFS to return the solution path and number of expanded nodes. | Completed |
| DFS implementation | Implemented DFS with a depth limit of 400 and node counting. | Completed |
| Timing | Used `time.perf_counter()` for per-run timing. | Completed |
| Profiling | Used `py-spy` sampling profiler to inspect runtime behavior. | Completed |
| Test cases | Used 10x10, 18x18 and 26x26 maze sizes. | Completed |
| Repeated runs | Used 5 runs per algorithm per test case. | Completed |
| Results checking | Reviewed and reran the code and checked the reported measurements. | Completed |
| Analysis | Compared execution time, nodes expanded and path length. | Completed |
| Documentation | Prepared the SLE-2 profiling report and repository documentation. | Completed |

## AI-Assisted Work

The SLE-2 report states that **Claude (Anthropic)** was used to assist with:

- Maze generator code
- BFS/DFS solver code
- `py-spy` profiling driver
- Maze, flame-graph and comparison-chart figures
- Report drafting and document formatting

The report also states that the student:

- Chose BFS vs DFS as the comparison pair.
- Chose the three maze sizes.
- Reviewed and reran the generated code.
- Confirmed the reported numbers.
- Checked that the flame graph matched the timing data.
- Wrote the justification based on the observed results.

## GitHub Commit Suggestions

Suggested commit history:

```text
Initial project setup
Add maze generator and BFS/DFS implementation
Add execution-time and node-count profiling
Add py-spy profiling driver
Add comparison results and documentation
Update README and contribution log
```
