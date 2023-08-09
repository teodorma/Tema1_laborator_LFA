# Tema1_laborator_LFA

Pentru un automat finit determinist si un cuvânt dat, sa se determine daca acel cuvânt este acceptat de
catre automat (dacã apartine sau nu limbajului recunoscut de automat). 
Daca acesta este acceptat, se va
afisa drumul folosit pentru acceptare, alternativ se va afisa un mesaj corespunzator.

Input: automatul (important, trebuie citit graful, am läsat un model la al doilea exemplu), dar poate sà fie
sub orice format doriti - atunci când veti prezenta eu va voi da automatul desenat si il veti putea
transforma.

Hint: incercati sa cititi automatul din fisier - gânditi-va la ce ar trebui programul vostru sa stie despre
automat pentru a il putea construi in memorie.

Cerinta bonus (+2p): Programul va ave acelasi comportament pentru un automat finit nedeterminist si
se vor afisa toate drumurile pentru acceptare (cerinta se refer strict la AFN, nu 1-AFN - desi va incurajez
sa incercati sa vedeti daca puteti trata si lambda tranzitle).
Prezentare: dupa ce terminati tema, va rog sa va treceti in acest sheet atunci când veti vrea sa prezentati
(cate un sheet pentru flecare grupa).

Exemplu 1:

![image](https://github.com/teodorma/LFA-tema1/assets/108132918/f7f475ad-25c7-4e86-8c58-653363f49f50)

    Input: bbabbabba = acceptat (afisam drum)
    Input: abbabba = acceptat (afisam drum)
    Input: ababababababaaaaaba = neacceptati
    Input: bbobbbaaaaabbbabbaaaaaaab = acceptat (afisam drum)

Exemplu 2:

    Input: 110001010 = neacceptat
    Input: 110101002 = acceptat (afisam drum)
    Input: 10101010 = acceptat (afisam drum)

## Exemplu de fisier de intrare pentru automat

    q0 1 g0 # Tranzitii
    90 0 g1
    q1 1 g0
    91 0 92
    92 2 a3
    q1 g3 # Starile finale

