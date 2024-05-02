# 10'luk tabanda girilen sayının 16'lık ve 2'lik tabanda değerini yazan program

# Onluk tabandan istenilen tabana çevirme yaparken sayıyı(onluk tabandaki) istenilen sayi değerine sonuç 1 olana kadar böleriz. Sonra en sağdan sola yazıp bitiririz
# biz işlemi pc ye yaptırdığımızda soldan sağa yazdırmış oluruz bu yüzden ters çevirmemiz gerekir. [::-1] kullanmak istediğim için sayıları str ye çevirdim
# çünkü [::-1] komutu sadece dizi,liste ve str veri tiplerinde kullanılabilir.


def ikilik_tabana_cevirme(x):
    # İkilik tabana dönüşüm yapılıyor
    ikilik = ""
    while x >= 1:  # Sonuç 1'den büyük olduğu sürece devam et
        ikilik += str(x % 2)  # Kalanı string olarak ekle
        x = x // 2  # Sayıyı 2'ye böl
    return ikilik[::-1]  # Sonucu ters çevir ve döndür


def onaltilik_tabana_cevirme(x):

    onaltilik=""
    while x>=1:
        kalan=x%16
        x=x//16
        if kalan>9:
            if kalan==10:
                kalan="A"
            elif kalan==11:
                kalan="B"
            elif kalan==12:
                kalan="C"
            elif kalan==13:
                kalan="D"
            elif kalan==14:
                kalan="E"
            elif kalan==15:
                kalan="F"
            onaltilik+=kalan
        else:
            y=str(kalan)  #10 dan önceki ifadelerin harf karşılığı olmadığı için str ye çevirmek zorundayız
            onaltilik+=y 
        ters_cevir=onaltilik[::-1] #ters çevirdik
    print("On altılık taban:",ters_cevir, end="")
            

    # Onaltılık tabana dönüşüm için harf-karakter eşleştirmesi
    hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    onaltilik = ""
    while x > 0:  # Sonuç 0'dan büyük olduğu sürece devam et
        kalan = x % 16
        # Kalan 9'dan büyükse harfle değiştir, değilse direk ekle
        onaltilik += hex_map.get(kalan, str(kalan))
        x = x // 16  # Sayıyı 16'ya böl
    return onaltilik[::-1]  # Sonucu ters çevir ve döndür



# Kullanıcıdan sayı al
sayi = int(input("Sayi girisi yapiniz: "))

# İkilik ve onaltılık tabana dönüşüm sonuçlarını yazdır
print("\nİkilik taban:", ikilik_tabana_cevirme(sayi))
print("On altılık taban:", onaltilik_tabana_cevirme(sayi))

# seninle grur duyuyorum bebişim muah <3
