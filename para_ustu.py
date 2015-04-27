@@ -6,13 +6,21 @@
    # Para birimi listesinin büyükten küçüğe doğru harekete ettigini varsayıyoruz

def Para(verilen_para,masraf):
    birim=[17,15,1]
    birim=[17,15,1]  # birimi buyukten kucuge dogru yaziniz
    para_ustu=verilen_para-masraf
    bolunen_liste=[]
    kalan_liste=[]
    for i in range(len(birim)):
        a=para_ustu/birim[i]
        bolunen_liste.append(a)
        return bolunen_liste
    sonuc=[]
    for i in birim:
        a = para_ustu / i
        if a > 0 :
            sonuc.append(a)
            sonuc.append(i)
            para_ustu =  para_ustu % i
    return sonuc
        
print(Para(100,55))
print(Para(100,0))


# Sonuçtan bahsetmek gerekirse ;
# Bu halde çıktı [5, 17, 1, 15] böyle olacaktır burada listenin ilk elemanı
# kaç adet ikinci elemandan verileceğini gösteriyor
# örneğin bu listede (" 5 tane 17 lik banknot , 1 tane 15 lik banknot ")
