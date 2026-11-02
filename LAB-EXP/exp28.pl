symptom(ravi, fever).
symptom(ravi, cough).
symptom(ravi, cold).

symptom(raju, fever).
symptom(raju, headache).
symptom(raju, bodypain).

symptom(anu, sneezing).
symptom(anu, cold).

disease(Person, flu) :-
    symptom(Person, fever),
    symptom(Person, cough),
    symptom(Person, cold).

disease(Person, malaria) :-
    symptom(Person, fever),
    symptom(Person, headache),
    symptom(Person, bodypain).

disease(Person, common_cold) :-
    symptom(Person, sneezing),
    symptom(Person, cold).

diagnose(Person) :-
    disease(Person, Disease),
    write('Person: '),
    write(Person),
    nl,
    write('Possible Disease: '),
    write(Disease),
    nl.