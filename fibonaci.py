fibo = 0
NACI = 1
minuleCislo = 0

for i in range(30):
    print(fibo)
    #print(NACI)
    #print(minuleCislo)

    if(fibo!=0):
        print(minuleCislo/fibo)

    minuleCislo = fibo + NACI



    fibo = NACI
    NACI = minuleCislo