# Basit hesap makinası programı
def toplama(sayilar):
    return sum(sayilar)


def cikarma(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc -= sayi
    return sonuc


def carpma(sayilar):
    sonuc = 1
    for sayi in sayilar:
        sonuc *= sayi
    return sonuc


def bolme(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc /= sayi
    return sonuc


def us_alma(taban, us):
    return taban**us


def karekok(sayi):
    return sayi**0.5


def sayilari_al(n):
    return [int(input("> ")) for _ in range(n)]


islem_sec = input(
    """Yapmak istediğiniz işlemi seçiniz:

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme 
5. Üs Alma 
6. Karekök
"""
)

if islem_sec == "1":
    n = int(input("Kaç sayı ile işlem yapacaksınız? "))
    print("İşlem yapmak istediğiniz sayıları giriniz:")
    print("Sonuç:", toplama(sayilari_al(n)))

elif islem_sec == "2":
    n = int(input("Kaç sayı ile işlem yapacaksınız? "))
    print("İşlem yapmak istediğiniz sayıları giriniz:")
    print("Sonuç:", cikarma(sayilari_al(n)))

elif islem_sec == "3":
    n = int(input("Kaç sayı ile işlem yapacaksınız? "))
    print("İşlem yapmak istediğiniz sayıları giriniz:")
    print("Sonuç:", carpma(sayilari_al(n)))

elif islem_sec == "4":
    n = int(input("Kaç sayı ile işlem yapacaksınız? "))
    print("İşlem yapmak istediğiniz sayıları giriniz:")
    print("Sonuç:", bolme(sayilari_al(n)))

elif islem_sec == "5":
    taban = int(input("Taban değeri giriniz: "))
    us = int(input("Kuvvet(üs) değeri giriniz: "))
    print("Sonuç:", us_alma(taban, us))

elif islem_sec == "6":
    sayi = int(input("İşlem yapmak istediğiniz sayıyı giriniz: "))
    print("Sonuç:", karekok(sayi))

else:
    print("Hatalı giriş yaptınız")
