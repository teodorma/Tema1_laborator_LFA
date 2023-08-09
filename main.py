f = open('Input.txt','r')
l=[[x for x in linie.split()] for linie in f.readlines()]
f.close()

stareFinala  = ''
stareCurenta = 'q0'
drum = []
aux = 0
cuvant = input("Cuvantul citit este:")

for x in cuvant:
    ok = 0
    for i in range(len(l)-1):
        if stareCurenta == l[i][0] and x == l[i][1] and ok == 0:
            drum.append(stareCurenta)
            stareCurenta = l[i][2]
            stareFinala = l[i][2]
            ok+=1
            break
    if ok == 0:
        aux = 1
        break
        
drum.append(stareFinala)
if stareFinala in l[len(l)-2] and aux == 0:
    print("Cuvantul "+cuvant+" este acceptat")
    print("Drumul este: "+str(drum))
else:
    print("Cuvant neacceptat")
