# Comparison – Prolog vs ASP Navigation Engines

## Prolog (nav_solver.pl)

### Strengths:
- Natural recursion (DFS implementation).
- Simple path construction.
- Returns explicit ordered paths.
- Ideal for interactive querying.

### Limitations:
- No built-in optimization.
- Must manually avoid cycles.
- Always returns first valid solution unless backtracked.

---

## ASP (nav_model.lp)

### Strengths:
- Constraint-driven reasoning.
- Generates multiple candidate models.
- Built-in minimization using #minimize.
- Guarantees shortest-step solution.
- Declarative semantics simplifies reasoning.

### Limitations:
- Syntax more complex for beginners.
- Requires careful control of recursion to avoid explosion.

---

## Key Differences

| Feature           | Prolog                     | ASP (Clingo)                       |
|------------------|----------------------------|------------------------------------|
| Recursion        | Procedural DFS             | Declarative reachability           |
| Optimization     | Manual                     | Built-in (#minimize)               |
| Model Type       | Single solution            | Multiple answer sets               |
| Best Use Case    | Exploration, queries       | Optimization, constraints           |

---

## Conclusion

Both systems successfully compute campus routes, but provide different
perspectives:

- Prolog excels in recursive exploration.
- ASP excels in optimization and constraint satisfaction.

The combination demonstrates how logic programming supports 
intelligent navigation tasks.

