
% ----- Locations (optional, just for clarity) -----
loc(library; quad; engineering; cafeteria; auditorium; parking; gym).

% ----- Undirected Edges on Campus -----
edge(library, quad).
edge(quad, engineering).
edge(engineering, cafeteria).
edge(cafeteria, auditorium).
edge(quad, gym).
edge(gym, parking).
edge(parking, auditorium).

% Make edges bi-directional
conn(X,Y) :- edge(X,Y).
conn(X,Y) :- edge(Y,X).

% ----- Start and Goal -----
start(library).
goal(auditorium).

% ----- Choose which connections are used as path steps -----
% step(X,Y) = we decide to use the connection X -> Y as part of our route
{ step(X,Y) : conn(X,Y) }.

% ----- Reachability (recursive) -----
% reach(S, X) means X is reachable from start S via chosen steps

reach(S,S) :- start(S).
reach(S,Y) :- reach(S,X), step(X,Y).

% We require that the goal must be reachable from the start
:- start(S), goal(G), not reach(S,G).

% ----- Prevent trivial self-loops -----
:- step(X,X).

% ----- Optimization -----
% Minimize number of steps used in the path (encourages shorter routes)
#minimize { 1,X,Y : step(X,Y) }.

#show step/2.
#show reach/2.
#show conn/2.
