"""
SLE-2: BFS vs DFS Maze Profiling

Course: 02AML204 -- Introduction to Artificial Intelligence
Student: MohammedSaad Bijapure
PRN: 25UAM101
Division: B

This script:
- Generates perfect mazes.
- Solves them with BFS and depth-limited DFS.
- Counts expanded nodes.
- Measures execution time with time.perf_counter().
- Repeats each test five times.
- Saves results to results.json.
- Creates a comparison chart when matplotlib is available.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import json
import random
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

Cell = Tuple[int, int]
Maze = Dict[Cell, List[Cell]]

SIZES = [10, 18, 26]
RUNS = 5
DFS_LIMIT = 400
SEED = 25_101


@dataclass
class Result:
    size: int
    algorithm: str
    average_ms: float
    average_nodes: float
    average_path_length: float


def generate_perfect_maze(size: int, rng: random.Random) -> Maze:
    """Generate a perfect maze as a graph of connected cells."""
    maze: Maze = {
        (r, c): []
        for r in range(size)
        for c in range(size)
    }

    start = (0, 0)
    visited = {start}
    stack = [start]

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    while stack:
        current = stack[-1]
        r, c = current

        candidates = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            nxt = (nr, nc)
            if 0 <= nr < size and 0 <= nc < size and nxt not in visited:
                candidates.append(nxt)

        if not candidates:
            stack.pop()
            continue

        nxt = rng.choice(candidates)

        maze[current].append(nxt)
        maze[nxt].append(current)

        visited.add(nxt)
        stack.append(nxt)

    return maze


def get_neighbors(maze: Maze, cell: Cell) -> List[Cell]:
    """Return only cells connected by carved/open maze passages."""
    return maze[cell]


def reconstruct_path(
    came_from: Dict[Cell, Optional[Cell]],
    goal: Cell,
) -> List[Cell]:
    """Reconstruct a path from start to goal."""
    if goal not in came_from:
        return []

    path = []
    current: Optional[Cell] = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


def bfs(
    maze: Maze,
    start: Cell,
    goal: Cell,
) -> Tuple[List[Cell], int]:
    """Breadth-First Search. Returns (path, nodes_expanded)."""
    frontier = deque([start])
    came_from: Dict[Cell, Optional[Cell]] = {start: None}
    nodes_expanded = 0

    while frontier:
        current = frontier.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in get_neighbors(maze, current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                frontier.append(neighbor)

    return reconstruct_path(came_from, goal), nodes_expanded


def dfs(
    maze: Maze,
    start: Cell,
    goal: Cell,
    depth_limit: int = DFS_LIMIT,
) -> Tuple[List[Cell], int]:
    """Depth-limited DFS. Returns (path, nodes_expanded)."""
    stack = [(start, 0)]
    came_from: Dict[Cell, Optional[Cell]] = {start: None}
    depth_seen = {start: 0}
    nodes_expanded = 0

    while stack:
        current, depth = stack.pop()
        nodes_expanded += 1

        if current == goal:
            return reconstruct_path(came_from, goal), nodes_expanded

        if depth >= depth_limit:
            continue

        neighbors = get_neighbors(maze, current)

        for neighbor in reversed(neighbors):
            new_depth = depth + 1

            if neighbor not in depth_seen or new_depth < depth_seen[neighbor]:
                depth_seen[neighbor] = new_depth
                came_from[neighbor] = current
                stack.append((neighbor, new_depth))

    return [], nodes_expanded


def benchmark(size: int, algorithm: str, runs: int = RUNS) -> Result:
    """Run one algorithm repeatedly on the same generated maze."""
    rng = random.Random(SEED + size)
    maze = generate_perfect_maze(size, rng)

    start = (0, 0)
    goal = (size - 1, size - 1)

    times = []
    nodes = []
    path_lengths = []

    for _ in range(runs):
        t0 = time.perf_counter()

        if algorithm == "BFS":
            path, expanded = bfs(maze, start, goal)
        elif algorithm == "DFS":
            path, expanded = dfs(maze, start, goal, DFS_LIMIT)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")

        elapsed_ms = (time.perf_counter() - t0) * 1000

        if not path:
            raise RuntimeError(
                f"{algorithm} did not find a path in the {size}x{size} maze."
            )

        times.append(elapsed_ms)
        nodes.append(expanded)
        path_lengths.append(len(path) - 1)

    return Result(
        size=size,
        algorithm=algorithm,
        average_ms=sum(times) / len(times),
        average_nodes=sum(nodes) / len(nodes),
        average_path_length=sum(path_lengths) / len(path_lengths),
    )


def save_results(results: List[Result]) -> None:
    data = [
        {
            "maze_size": f"{r.size}x{r.size}",
            "algorithm": r.algorithm,
            "average_time_ms": round(r.average_ms, 6),
            "average_nodes_expanded": round(r.average_nodes, 3),
            "average_path_length": round(r.average_path_length, 3),
        }
        for r in results
    ]

    Path("results.json").write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )


def create_chart(results: List[Result]) -> None:
    """Create a simple BFS vs DFS average-time chart."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib is not installed; skipping chart generation.")
        return

    sizes = [f"{s}x{s}" for s in SIZES]
    bfs_times = [
        next(r.average_ms for r in results if r.size == s and r.algorithm == "BFS")
        for s in SIZES
    ]
    dfs_times = [
        next(r.average_ms for r in results if r.size == s and r.algorithm == "DFS")
        for s in SIZES
    ]

    x = list(range(len(SIZES)))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar([i - width / 2 for i in x], bfs_times, width, label="BFS")
    plt.bar([i + width / 2 for i in x], dfs_times, width, label="DFS")
    plt.xticks(x, sizes)
    plt.ylabel("Average execution time (ms)")
    plt.xlabel("Maze size")
    plt.title("Average execution time: BFS vs DFS")
    plt.legend()
    plt.tight_layout()
    plt.savefig("comparison_chart.png", dpi=200)
    plt.close()


def main() -> None:
    results: List[Result] = []

    print("SLE-2: BFS vs DFS Maze Profiling")
    print("=" * 45)

    for size in SIZES:
        for algorithm in ("BFS", "DFS"):
            result = benchmark(size, algorithm)
            results.append(result)

            print(
                f"{size}x{size} | {algorithm:3s} | "
                f"{result.average_ms:.4f} ms | "
                f"nodes: {result.average_nodes:.1f} | "
                f"path: {result.average_path_length:.1f}"
            )

    save_results(results)
    create_chart(results)

    print("\nSaved: results.json")
    print("Saved: comparison_chart.png (if matplotlib is installed)")


if __name__ == "__main__":
    main()
