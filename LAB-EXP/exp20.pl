% Planet database
planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

% Planet types
type(mercury, terrestrial).
type(venus, terrestrial).
type(earth, terrestrial).
type(mars, terrestrial).
type(jupiter, gas_giant).
type(saturn, gas_giant).
type(uranus, ice_giant).
type(neptune, ice_giant).

% Rule to find planet position
position(Planet, Number) :-
    planet(Planet, Number).

% Rule to find planet type
planet_type(Planet, Type) :-
    type(Planet, Type).

% Rule to find terrestrial planets
terrestrial(Planet) :-
    type(Planet, terrestrial).