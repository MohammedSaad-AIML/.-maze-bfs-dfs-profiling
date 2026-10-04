# SLE-3: Architectural Design (Full C4 Model)

**Course:** 02AML204 — Introduction to Artificial Intelligence  
**PRN:** 25UAM101  
**Name:** MohammedSaad Bijapure  
**Division:** B  
**System:** BFS vs DFS Maze Solving and Profiling

## 1. System Title & Short Description

The BFS vs DFS Maze Solving System generates a perfect maze and finds a path from the top-left start cell to the bottom-right goal cell. It implements Breadth-First Search (BFS) and depth-limited Depth-First Search (DFS). The system measures execution time, nodes expanded, and solution path length for different maze sizes. The profiling results are used to compare the runtime behavior of the two search strategies.

## 2. Context Diagram — C4 Level 1

~~~mermaid
flowchart LR
    U[User / Student] -->|Provides maze experiment request| S[BFS vs DFS Maze Solving System]
    S -->|Returns path and performance results| U
    S -.->|Uses| P[Python Runtime]
~~~

### Explanation
The user runs the maze experiment and receives the solution path and measured performance results. The main system contains the maze generation, search, measurement, and reporting functionality. Python provides the runtime environment.

## 3. Container Diagram — C4 Level 2

~~~mermaid
flowchart LR
    U[User] --> I[Input / Experiment Controller]
    I --> M[Maze Generator]
    M --> E[Search Engine]
    E --> R[Result & Path Processor]
    R --> O[Output / Report Module]
    E --> T[Performance Measurement]
    T --> O
~~~

### Container Responsibilities

- **Input / Experiment Controller:** Starts the experiment and selects maze sizes and algorithms.
- **Maze Generator:** Creates the perfect maze graph using randomized depth-first generation.
- **Search Engine:** Runs BFS or depth-limited DFS to search from start to goal.
- **Result & Path Processor:** Reconstructs the solution path and collects node-expansion information.
- **Performance Measurement:** Measures execution time using time.perf_counter() and organizes benchmark values.
- **Output / Report Module:** Saves results.json and creates the comparison chart.

## 4. Component Diagram — C4 Level 3

The most important container is the **Search Engine**.

~~~mermaid
flowchart TB
    SE[Search Engine]
    SE --> F[Frontier]
    SE --> V[Visited / Depth Set]
    SE --> G[Goal Test]
    SE --> N[Neighbor Expansion]
    SE --> PR[Path Reconstructor]
    F --> N
    N --> V
    N --> G
    G --> PR
~~~

### Component Explanation

The Frontier stores pending search states: a queue for BFS and a stack for DFS. The visited/depth structure prevents unnecessary repeated exploration. Neighbor Expansion obtains connected maze cells, while Goal Test checks whether the destination has been reached. Path Reconstructor follows parent information to produce the final path.

## 5. Code Level Overview — C4 Level 4

- generate_perfect_maze() — creates the connected maze graph.
- get_neighbors() — returns cells connected to a maze cell.
- bfs() — performs Breadth-First Search.
- dfs() — performs depth-limited Depth-First Search.
- reconstruct_path() — rebuilds the path from parent information.
- benchmark() — repeats tests and calculates average measurements.
- save_results() — writes benchmark results to results.json.
- create_chart() — generates the BFS vs DFS comparison chart.

## 6. Design Decisions

The SLE-3 architecture continues the same BFS/DFS maze system used for SLE-2 so that the architecture directly represents the profiled implementation. The Search Engine is separated conceptually from maze generation, measurement, and output to make the system easier to understand. BFS uses a queue, while DFS uses a stack with a depth limit of 400. A separate path-reconstruction function keeps search logic and result construction clear.

## 7. AI Contribution Note

**AI tools used:** AI coding assistant / ChatGPT support.

**What AI helped with:** Assistance was used for parts of the maze generator, BFS/DFS solver, profiling driver, figures, and report drafting.

**What I did myself:** I selected the BFS/DFS comparison, selected the maze sizes, reviewed and reran the generated code, checked the measured results, and used the results to justify the comparison and architecture.

## 8. Conclusion

The C4 model shows the BFS/DFS maze system from its overall user interaction down to its main functions. The four levels make the relationship between maze generation, search, measurement, path reconstruction, and output clear. The architecture also connects directly with the SLE-2 profiling work. This helped demonstrate how an AI search program can be organized into understandable software components.

## SLE-2 Results Used as Architectural Context

| Maze | Algorithm | Avg. time (ms) | Nodes expanded | Path length |
|---|---|---:|---:|---:|
| 10x10 | BFS | 0.0720 | 39 | 32 |
| 10x10 | DFS | 0.0993 | 44 | 32 |
| 18x18 | BFS | 0.1989 | 117 | 100 |
| 18x18 | DFS | 0.7283 | 190 | 100 |
| 26x26 | BFS | 0.5616 | 349 | 190 |
| 26x26 | DFS | 4.3170 | 674 | 190 |

## Submission Checklist

- [x] System description
- [x] C4 Level 1 — Context
- [x] C4 Level 2 — Container
- [x] C4 Level 3 — Component
- [x] C4 Level 4 — Code
- [x] Design decisions
- [x] AI contribution note
- [x] Conclusion
- [x] Connected to SLE-2 BFS/DFS Maze work
