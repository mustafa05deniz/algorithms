
# Merge sort yani kabuk sıralama kodudur . 

def bol(liste):
    if len(liste)>1:
        orta_nokta=len(liste)//2
        sol_taraf=liste[:orta_nokta]
        sag_taraf=liste[orta_nokta:]

        bol(sol_taraf)
        bol(sag_taraf)

        a,b,c=0,0,0
        while a<len(sol_taraf) and b<len(sag_taraf):
            if sol_taraf[a] < sag_taraf[b]:
                liste[c] = sol_taraf[a]
                a=a+1
            else:
                liste[c]=sag_taraf[b]
                b=b+1
            c=c+1

        while a<len(sol_taraf):
            liste[c]=sol_taraf[a]
            a=a+1
            c=c+1
        while b<len(sag_taraf):
            liste[c]=sag_taraf[b]
            b=b+1
            c=c+1
    print(liste)


bol([21,344,4,12,32,54,16,34,75])   # ornek liste 
