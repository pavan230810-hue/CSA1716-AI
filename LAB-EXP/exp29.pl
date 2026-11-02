fact(sunny).
fact(warm).

rule1 :-
    fact(sunny),
    fact(warm),
    assertz(fact(go_outdoors)).

rule2 :-
    fact(go_outdoors),
    assertz(fact(play)).

forward :-
    rule1,
    rule2.