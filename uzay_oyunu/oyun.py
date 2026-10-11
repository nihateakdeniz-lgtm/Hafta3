import json
from .araclar import hamle_sayaci

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """
    Eşya durumuna göre envanter metni oluşturur. (Görev 1)
    """
    metin = "Sende:"
    if credits: metin += " bol kredi,"
    if engines: metin += " hiperdrive,"
    if copilot: metin += " yetenekli bir pilot"
    
    if metin == "Sende:":
        return ""
    return metin + " "

def hedef_menusu(hedefler: list[str]) -> str:
    """
    Gidilebilecek hedefleri numaralandırılmış menü olarak döndürür. (Görev 1)
    """
    menu = "Nereye gitmek istersin?\n"
    for i, hedef in enumerate(hedefler, 1):
        menu += f"[{i}] {hedef} "
    return menu.strip()

def galaksi_kur(gezegenler: list[str], baglantilar: dict[str, list[str]], baslangic: str, **kwargs) -> dict:
    """
    Galaksi verilerini doğrular ve oyun durumunu döndürür. (Görev 3)
    """
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde yok!")
        
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }

def travel(galaksi: dict) -> None:
    """
    Oyunun ana döngüsü. (Refactored)
    """
    sayac = hamle_sayaci()
    while True:
        mevcut = galaksi["konum"]
        hedefler = galaksi["baglantilar"][mevcut]
        
        print(f"\nŞu an: {mevcut.upper()}")
        print(envanter_metni(True, False, True))
        print(hedef_menusu(hedefler))
        
        # Basit bir test döngüsü, gerçek oyunda input() kullanılır.
        break 
        
    print(f"Oyunu {sayac()} hamlede bitirdin!")