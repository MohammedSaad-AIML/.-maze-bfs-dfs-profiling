# SLE-3 C4 Diagrams

## Level 1 — Context
~~~mermaid
flowchart LR
U[User / Student] -->|Experiment request| S[BFS vs DFS Maze Solving System]
S -->|Path + performance result| U
S -.-> P[Python Runtime]
~~~

## Level 2 — Container
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

## Level 3 — Component
~~~mermaid
flowchart TB
SE[Search Engine] --> F[Frontier]
SE --> V[Visited / Depth Set]
SE --> G[Goal Test]
SE --> N[Neighbor Expansion]
SE --> PR[Path Reconstructor]
F --> N
N --> V
N --> G
G --> PR
~~~

## Level 4 — Code
~~~text
generate_perfect_maze()
get_neighbors()
bfs()
dfs()
reconstruct_path()
benchmark()
save_results()
create_chart()
~~~
