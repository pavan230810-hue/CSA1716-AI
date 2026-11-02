bird(parrot).
bird(pigeon).
bird(crow).
bird(ostrich).
bird(penguin).
bird(sparrow).

can_fly(parrot).
can_fly(pigeon).
can_fly(crow).
can_fly(sparrow).

cannot_fly(ostrich).
cannot_fly(penguin).

check(X) :-
    bird(X),
    can_fly(X),
    write(X),
    write(' can fly.').

check(X) :-
    bird(X),
    cannot_fly(X),
    write(X),
    write(' cannot fly.').