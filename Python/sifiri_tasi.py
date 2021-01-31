def kabarcik_sirala(vektor):
    for i in range(len(vektor)-1):
        for j in reversed(range(i+1, len(vektor))):
            if vektor[j] == 0:
                depo = vektor[j-1]
                vektor[j-1] = vektor[j]
                vektor[j] = depo
                #print(vektor) Algoritmanın adımlarını görmek için.
    print(vektor)

vekt = [2,4,1,6,4,0,0]
kabarcik_sirala(vekt)