
% ----- Campus Locations -----
location(library).
location(quad).
location(engineering).
location(cafeteria).
location(auditorium).
location(parking).
location(gym).

% ----- Undirected Paths (Bi-directional edges) -----
path(library, quad).
path(quad, engineering).
path(engineering, cafeteria).
path(cafeteria, auditorium).
path(quad, gym).
path(gym, parking).
path(parking, auditorium).

% Make the path symmetric
connected(X, Y) :- path(X, Y).
connected(X, Y) :- path(Y, X).

/*
   ROUTE FINDER
*/

route(Start, End, Route) :-
    travel(Start, End, [Start], RevRoute),
    reverse(RevRoute, Route).

% Base case: direct connection
travel(Node, Node, Visited, Visited).

% Recursive expansion
travel(Current, Goal, Visited, FinalPath) :-
    connected(Current, Next),
    \+ member(Next, Visited),
    travel(Next, Goal, [Next | Visited], FinalPath).

