diet(diabetes, 'Low sugar and high fibre food').
diet(obesity, 'Low calorie food and vegetables').
diet(anemia, 'Iron rich foods like spinach and dates').
diet(hypertension, 'Low salt food and fresh fruits').
diet(heart_disease, 'Low fat food and whole grains').
diet(ulcer, 'Soft food and avoid spicy food').

suggest_diet(Disease) :-
    diet(Disease, Food),
    write('Disease: '),
    write(Disease),
    nl,
    write('Suggested Diet: '),
    write(Food),
    nl.

suggest_diet(Disease) :-
    \+ diet(Disease, _),
    write('No diet information available.').