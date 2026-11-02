% Student details
student(101, arun).
student(102, bala).
student(103, kumar).

% Teacher details
teacher(t1, ramesh).
teacher(t2, suresh).
teacher(t3, priya).

% Subject codes
subject(c101, computer_science).
subject(c102, mathematics).
subject(c103, physics).

% Teaching relationship
teaches(t1, c101).
teaches(t2, c102).
teaches(t3, c103).

% Student subject relationship
studies(101, c101).
studies(102, c102).
studies(103, c103).

% Rule to find teacher for a student
student_teacher(Student, Teacher) :-
    studies(Student, Code),
    teaches(Teacher, Code).

% Rule to find subject name
student_subject(Student, Subject) :-
    studies(Student, Code),
    subject(Code, Subject).