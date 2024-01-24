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
