fact(sunny).
fact(warm).

can_go_outdoors :-
    fact(sunny),
    fact(warm).

can_play :-
    can_go_outdoors.

happy :-
    can_play.