
# Para üstü problemi Verilen bir Paradan masrafı çıkardığında geriye kalan para üstünün hangi banknotlar halinde verileceğini 
# çözen bir algoritma 

# Kriterler : 
    # Para birimi listesinin büyükten küçüğe doğru harekete ettigini varsayıyoruz

def Para(verilen_para,masraf):
    birim=[17,15,1]
    para_ustu=verilen_para-masraf
    bolunen_liste=[]
    kalan_liste=[]
    for i in range(len(birim)):
        a=para_ustu/birim[i]
        bolunen_liste.append(a)
        return bolunen_liste
        
print(Para(100,55))
