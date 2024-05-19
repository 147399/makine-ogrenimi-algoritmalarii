from random import randint

"""
    Küçük çapta bir çarpım tablosu uygulaması
"""

print("-" * 50)
print("\t\tHOŞGELDİNİZ..")
print("-" * 50, "\n")


def carpim(sayi1, sayi2, cevap):
    """
    İki sayının çarpımını hesaplar ve kullanıcının verdiği cevapla kontrol eder.

    Args:
        sayi1 (int): İlk sayı.
        sayi2 (int): İkinci sayı.
        cevap (str): Kullanıcının verdiği cevap.

    Returns:
        None
    """
    if cevap != "-1":
        sonuc = str(sayi1 * sayi2)
        if sonuc == cevap:
            print("\t\t***** Doğru *****")
        else:
            print("\t!!! Yanlış cevap %s olacaktı" % sonuc)
        
    else:
        secim()
    if cevap == "000":
       return

def basla(min_deger, max_deger):
    """
    Verilen aralıkta rastgele sayılar üreterek çarpım işlemlerini gerçekleştirir.

    Args:
        min_deger (int): Rastgele üretilecek sayıların minimum değeri.
        max_deger (int): Rastgele üretilecek sayıların maksimum değeri.

    Returns:
        None
    """
    for _ in range(0, 5):
        sayi1 = randint(min_deger, max_deger)
        sayi2 = randint(min_deger, max_deger)
        print("_" * 50, "\n")
        print("\t%d x %d kaça eşittir? (çıkış = 000)" % (sayi1, sayi2))
        cevap = input("sonuc >> ")
        carpim(sayi1, sayi2, cevap)

               # Kullanıcı "00" girdiğinde döngüyü sıfırla
        if cevap == "00":
            print("cıkıs yapılıyor...")
            print("-" * 50)
            return
        if _ == 4:
            print("\n *-- Bu bölüm bitti bir üst bölüme geçebilsiniz --*\n")
            secim()


def secim():
    """
    Kullanıcıdan hangi seviyeden başlamak istediğini seçmesini sağlar.

    Returns:
        None
    """
    print(" Hangi seviyeden başlamak istiyorsunuz (çıkış = 000) ?\n")
    print("  1 - Kolay ")
    print("  2 - Orta ")
    print("  3 - Zor")
    print("  4 - Çok zor\n")

    seviye = input(" >> ")

    if seviye == "1":
        basla(1, 10)
    elif seviye == "2":
        basla(5, 12)
    elif seviye == "3":
        basla(10, 25)
    elif seviye == "4":
        basla(10, 100)
    else:
        exit(0)


if __name__ == '__main__':
    secim()