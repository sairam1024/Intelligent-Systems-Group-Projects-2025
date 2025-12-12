# Methodology – Navigation Engine Implementation

## 1. Campus Graph Representation

The campus is modeled as a graph where:
- Nodes represent buildings.
- Edges represent walkable paths.

In both engines, connections are represented as undirected edges.

Example:
    library ↔ quad
    quad ↔ engineering
    engineering ↔ cafeteria
    cafeteria ↔ auditorium

This layout ensures multiple possible paths exist.

---

## 2. Prolog Engine

The Prolog solver uses a recursive DFS approach:

### Key components:
- `connected/2` defines bidirectional access.
- `route/3` constructs a path from start to goal.
- `travel/4` recurses until the target is reached.
- Cycle avoidance is handled using visited lists.

### Why Prolog works well here:
- Recursion is natural and compact.
- Backtracking automatically explores path alternatives.
- Output includes exact path order.

---

## 3. ASP Engine (Clingo)

The ASP model searches for paths by selecting a subset of edges (`step/2`)
and checks reachability using recursive rules.

### Key components:
- `conn/2` defines undirected edges.
- `step/2` selects which edges form the route.
- `reach/2` recursively determines reachable nodes.
- Constraint ensures the goal is reachable.
- `#minimize` finds the shortest set of edges connecting start to goal.

### Why ASP is suited:
- Ideal for constraint-heavy problems.
- Produces multiple candidate models.
- Optimization is built-in.

---

## 4. Optimization Strategy

ASP minimizes the number of steps:

#minimize { 1,X,Y : step(X,Y) }.    

This ensures:
- Only essential edges are used.
- The selected path is the shortest in terms of steps/hops.

---

## 5. Output Interpretation

Prolog returns explicit paths:
P = [library, quad, engineering, cafeteria, auditorium].

ASP returns selected edges:
step(library,quad)
step(quad,engineering)
step(engineering,cafeteria)
step(cafeteria,auditorium)

Both represent the same navigation solution.
