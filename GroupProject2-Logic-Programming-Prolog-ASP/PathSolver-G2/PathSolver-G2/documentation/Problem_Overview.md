# Problem Overview – Campus Pathfinding Logic Engine

This project explores logic programming approaches for solving 
navigation problems on a simplified university campus layout. 
The task is to compute valid routes between buildings and determine 
the shortest walking path between two locations.

Two reasoning systems were developed:

1. **Prolog Navigation Solver**
   - Uses recursive depth-first exploration.
   - Finds valid routes by expanding connected paths.
   - Naturally supports backtracking and path reconstruction.

2. **ASP Navigation Model**
   - Uses Answer Set Programming (Clingo) to generate candidate paths.
   - Applies recursion through reachability rules.
   - Uses constraints to ensure valid routes.
   - Minimizes the number of steps to compute the shortest path.

This project demonstrates how logic programming languages can 
support reasoning, recursion, constraint satisfaction, 
and route optimization in a navigation context.

