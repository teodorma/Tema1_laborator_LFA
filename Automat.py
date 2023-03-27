f = open('Input.txt','r')
l=[[x for x in linie.split()] for linie in f.readlines()]
f.close()

stareFinala  = ''
stareCurenta = 'q0'
drum = []
cuvant = input("Cuvantul citit este:")
ok = 0

for x in cuvant:
    for i in range(len(l)-1):
        if stareCurenta == l[i][0] and x == l[i][1] and ok == 0:
            drum.append(stareCurenta)
            stareCurenta = l[i][2]
            stareFinala = l[i][2]
            break
          
if stareFinala in l[len(l)-1]:
    print("Cuvantul "+cuvant+" nu este acceptat")
    print("Drumul este: "+str(drum))
else:
    print("Cuvant neacceptat")
