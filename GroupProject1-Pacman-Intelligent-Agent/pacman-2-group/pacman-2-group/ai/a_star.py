import heapq
from config.constants import MAZE_LAYOUT


def heuristic(a, b):
    (r1, c1) = a
    (r2, c2) = b
    return abs(r1 - r2) + abs(c1 - c2)


def a_star_search(start, goal):
    rows = len(MAZE_LAYOUT)
    cols = len(MAZE_LAYOUT[0])

    def is_wall(r, c):
        return MAZE_LAYOUT[r][c] == "#"

    open_heap = []
    heapq.heappush(open_heap, (0, start))

    came_from = {start: None}
    g_score = {start: 0}

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current == goal:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = came_from[node]
            return path[::-1]

        r, c = current
        for dr, dc in directions:
            nr, nc = r+dr, c+dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if is_wall(nr, nc):
                continue

            new_cost = g_score[current] + 1
            if (nr, nc) not in g_score or new_cost < g_score[(nr, nc)]:
                g_score[(nr, nc)] = new_cost
                f_score = new_cost + heuristic((nr, nc), goal)
                heapq.heappush(open_heap, (f_score, (nr, nc)))
                came_from[(nr, nc)] = current

    return []
    