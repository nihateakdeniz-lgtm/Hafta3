import time

def hamle_sayaci():
    """
    Her çağrıldığında bir artan bir sayaç fonksiyonu döndürür (Closure). (Görev 5)
    """
    sayac = 0
    def sayac_artir():
        nonlocal sayac
        sayac += 1
        return sayac
    return sayac_artir

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """
    Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür. (Görev 5)
    """
    gezegenler = galaksi["gezegenler"]
    baglantilar = galaksi["baglantilar"]
    return sorted(gezegenler, key=lambda x: (-len(baglantilar[x]), x))

def sure_olc(fonksiyon):
    """
    Bir fonksiyonun çalışma süresini ölçen sarmalayıcı döndürür. (Bonus)
    """
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic:.4f} saniye sürdü.")
        return sonuc
    return wrapper

# Bonus testi
if __name__ == "__main__":
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)