edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(b, e, 5).
edge(c, f, 3).
edge(d, g, 2).
edge(e, g, 1).
edge(f, g, 2).

heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 5).
heuristic(d, 4).
heuristic(e, 3).
heuristic(f, 2).
heuristic(g, 0).

bestfirst(Start, Goal, Path) :-
    search([[Start]], Goal, ReversePath),
    reverse(ReversePath, Path).

search([[Goal | Rest] | _], Goal, [Goal | Rest]).

search([ [Node | Rest] | OtherPaths], Goal, Path) :-
    findall(
        [Next, Node | Rest],
        (edge(Node, Next, _),
         \+ member(Next, [Node | Rest])),
        NewPaths
    ),
    append(OtherPaths, NewPaths, AllPaths),
    sort_paths(AllPaths, SortedPaths),
    search(SortedPaths, Goal, Path).

sort_paths(Paths, Sorted) :-
    findall(H-P,
        (member(P, Paths),
         P = [Node | _],
         heuristic(Node, H)),
        Pairs),
    keysort(Pairs, SortedPairs),
    extract_paths(SortedPairs, Sorted).

extract_paths([], []).
extract_paths([_-P | T], [P | R]) :-
    extract_paths(T, R).