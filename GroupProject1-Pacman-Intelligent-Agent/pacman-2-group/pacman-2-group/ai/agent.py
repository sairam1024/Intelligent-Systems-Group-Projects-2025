from ai.a_star import a_star_search


class HunterAgent:
    def __init__(self, hunter, ghost):
        self.hunter = hunter
        self.ghost = ghost

    def update(self):
        target = (self.ghost.row, self.ghost.col)
        start = (self.hunter.row, self.hunter.col)

        path = a_star_search(start, target)
        if not path or len(path) < 2:
            return

        next_r, next_c = path[1]
        dr = next_r - self.hunter.row
        dc = next_c - self.hunter.col

        self.hunter.set_direction(dr, dc)
