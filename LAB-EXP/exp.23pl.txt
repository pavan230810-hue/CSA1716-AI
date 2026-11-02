male(john).
male(peter).
male(david).
male(james).

female(mary).
female(susan).
female(linda).

parent(john, peter).
parent(mary, peter).

parent(john, susan).
parent(mary, susan).

parent(peter, david).
parent(linda, david).

parent(peter, james).
parent(linda, james).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

child(X, Y) :-
    parent(Y, X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).