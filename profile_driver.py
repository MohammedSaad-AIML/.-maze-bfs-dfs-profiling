"""
py-spy driver for SLE-2 BFS/DFS profiling.

Run with:

py-spy record --rate 100 --duration 3 --output flame.svg -- python profile_driver.py
"""

from maze_profiling import (
    DFS_LIMIT,
    SIZES,
    bfs,
    dfs,
    generate_perfect_maze,
)
import random


def main() -> None:
    # Use the largest maze repeatedly so py-spy has enough
    # wall-clock execution time to collect samples.
    size = max(SIZES)
    rng = random.Random(25_101)
    maze = generate_perfect_maze(size, rng)

    start = (0, 0)
    goal = (size - 1, size - 1)

    for _ in range(20000):
        bfs(maze, start, goal)
        dfs(maze, start, goal, DFS_LIMIT)


if __name__ == "__main__":
    main()
