# Results – Campus Navigation System

## 1. Prolog Results

### Query:
?- route(library, auditorium, P).

### Output:
P = [library, quad, engineering, cafeteria, auditorium].

This confirms the recursive DFS correctly finds a valid route.

---

### Query:
?- route(engineering, parking, P).

Output:
P = [engineering, cafeteria, auditorium, parking].

---

### Query:
?- route(library, cafeteria, P).

Output:
P = [library, quad, engineering, cafeteria].

These results verify the solver can navigate multi-step routes,
avoid cycles, and compute correct paths.

---

## 2. ASP Results (Clingo)

### Execution:
clingo nav_model.lp

### Output Summary:
- 6 candidate models generated.
- Optimization values: 9 → 8 → 7 → 6 → 5 → 4
- Shortest solution uses 4 steps.

### Optimal Model:
step(library,quad)
step(quad,engineering)
step(engineering,cafeteria)
step(cafeteria,auditorium)
goal_dist = 4 steps
OPTIMUM FOUND

---

## Interpretation

Both engines agree on the shortest route:

**Library → Quad → Engineering → Cafeteria → Auditorium**

ASP confirms shortest path via optimization,
while Prolog constructs the full route explicitly.

These results satisfy all project goals:
- recursion
- reasoning
- constraints
- optimization
- valid path generation

