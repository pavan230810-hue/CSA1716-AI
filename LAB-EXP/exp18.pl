% Facts
person(ravi, '2002-05-10').
person(kumar, '2001-08-15').
person(raj, '2003-02-20').
person(anu, '2002-11-25').

% Rules
display(Name, DOB) :-
    person(Name, DOB).