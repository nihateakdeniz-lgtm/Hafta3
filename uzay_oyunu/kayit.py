def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> None:
    """
    Görev kaydını formatlayıp yazdırır. (Görev 2)
    """
    print(f"[{oncelik.upper()}] {baslik}")
    for i, adim in enumerate(adimlar, 1):
        print(f"{i}. {adim}")
    for anahtar, deger in ekler.items():
        print(f"{anahtar}: {deger}")

if __name__ == "__main__":
    # 1. Yöntem: Normal çağrı
    gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al", 
                oncelik="YÜKSEK", sorumlu="Ayşe")
    
    print("-" * 20)
    
    # 2. Yöntem: Listeyi ve sözlüğü açarak çağrı
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *adimlar_listesi, oncelik="YÜKSEK", **ek_bilgiler)