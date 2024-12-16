pai(jose, maria).
pai(jose, joao).
mae(ana, maria).
mae(ana, joao).
pai(marcos, jose).
mae(clarice, jose).
pai(pedro, ana).
mae(renata, ana).

eh_pai(Pai, Filho) :-
    pai(Pai, Filho).

eh_mae(Mae, Filho) :-
    mae(Mae, Filho).