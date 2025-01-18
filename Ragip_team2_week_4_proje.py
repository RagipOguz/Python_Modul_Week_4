#  main.py
from kitap_transaktions import kitaplar
from member_transactions import UyeIslemleri
from datetime import datetime, timedelta


def menu():
    print("Kütüphane Programı")
    print("1. Üye İşlemleri")
    print("2. Kitap İşlemleri")
    print("3. Çıkış")
    return int(input("Lütfen seçiminizi yapın (1, 2, 3): "))


def uye_menu():
    print("\nÜye İşlemleri")
    print("1. Üye Ekle")
    print("2. Üye Sil")
    print("3. Üye Kontrol")
    print("4. Üyeye Kitap Ver")
    print("5. Üyeden Kitap İade Al")
    print("6. Ana Menüye Dön")
    return int(input("Lütfen seçiminizi yapın (1-6): "))


def kitap_menu():
    print("\nKitap İşlemleri")
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Tüm Kitapları Listele")
    print("4. Teslim Süresi Hesapla")
    print("5. Ana Menüye Dön")
    return int(input("Lütfen seçiminizi yapın (1-5): "))


def kitap_teslim_suresi_hesapla(alinan_tarih, teslim_suresi_gun):
    alinan_tarih_obj = datetime.strptime(alinan_tarih, "%Y-%m-%d")
    teslim_tarihi = alinan_tarih_obj + timedelta(days=teslim_suresi_gun)
    return teslim_tarihi.strftime("%Y-%m-%d")


def main():
    while True:
        secim = menu()
        if secim == 1:
            uye_islemleri()
        elif secim == 2:
            kitap_islemleri()
        elif secim == 3:
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


def uye_islemleri():
    uye = UyeIslemleri()
    while True:
        secim = uye_menu()
        if secim == 1:
            uye.uye_ekle()
        elif secim == 2:
            uye.uye_sil()
        elif secim == 3:
            uye.uye_kontrol()
        elif secim == 4:
            uye.kitap_ver()
        elif secim == 5:
            uye.kitap_iade_al()
        elif secim == 6:
            print("Ana menüye dönülüyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


def kitap_islemleri():
    kitap = kitaplar()
    while True:
        secim = kitap_menu()
        if secim == 1:
            kitap.kitap_ekle()
        elif secim == 2:
            kitap.kitap_sil()
        elif secim == 3:
            kitap.tum_kitaplari_listele()
        elif secim == 4:
            alinan_tarih = input("Kitabın alındığı tarihi giriniz (YYYY-MM-DD): ")
            teslim_suresi = 14  # Teslim süresi sabit 14 gün
            teslim_tarihi = kitap_teslim_suresi_hesapla(alinan_tarih, teslim_suresi)
            print(f"Kitabın alındığı tarih: {alinan_tarih}")
            print(f"Kitabın teslim edilmesi gereken tarih: {teslim_tarihi}")
        elif secim == 5:
            print("Ana menüye dönülüyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


if _name_ == "_main_":
    main()


#  kitap_islemleri.py

# Error catching-file op., JSON module
# Two main parts membership transac. and book transac.
# Membership transac include adding member, deleting member, checking member, giving book to member, returned book from member
# Similar book transac.
# It will consist of main.py, Kitap_transactions.py, Member_Transactions.py, Zaman.py files.

import json


kitaplar = [
    {
        "Barkod": 9786053114772,
        "Dil": "Türkçe",
        "Fiyat": 20.4,
        "Kitap_Adi": "Süt Lekesi",
        "Yayinevi": "Destek Yayınları",
        "Yazar": "Esra Ezmeci"
    },
    {   
        "Barkod": 978605579064,
        "Dil": "Türkçe",
        "Fiyat": 20.4,
        "Kitap_Adi": "Yanlış Hayat Doğru Yaşanmaz",
        "Yayinevi": "Olimpos Yayınları",
        "Yazar": "Ethem Emin Nemutlu"
    },
    {
        "Barkod": 9786051856322,
        "Dil": "Türkçe",
        "Fiyat": 27.3,
        "Kitap_Adi": "Hazan",
        "Yayinevi": "Everest Yayınları",
        "Yazar": "Ayşe Kulin"
    },
    {
        "Barkod": 97897507513632,
        "Dil": "Türkçe",
        "Fiyat": 24.15,
        "Kitap_Adi": "Okçu'nun Yolu",
        "Yayinevi": "Can Yayınları",
        "Yazar": "Paulo Coelho"
    }
]

# JSON dosyasını UTF-8 olarak oluşturdum ve kaydettim
with open("kitap.json", "w", encoding="utf-8") as dosya:
    json.dump(kitaplar, dosya, ensure_ascii=False, indent=4)

#kitapları okuma
dosya_adi = "kitap.json"

def oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            return json.load(dosya)  # JSON verisini oku
    except FileNotFoundError:
            print("Dosya bulunamadı.")

#kitapları listeleme           
def kitaplari_listele():
    dosya_adi = "kitap.json"       
    kitaplar = oku(dosya_adi)       

    print("\n Kütüphanedeki Kitaplar:\n")
    for kitap in kitaplar:
        print(f" Kitap Adı: {kitap['Kitap_Adi']}")
        print(f" Yazar: {kitap['Yazar']}")
        print(f" Yayınevi: {kitap['Yayinevi']}")
        print(f" Barkod: {kitap['Barkod']}")
        print(f" Fiyat: {kitap['Fiyat']} TL")
        print(f"  Dil: {kitap['Dil']}")
        print("-" * 40)
kitaplari_listele()

#kitap ekleme
def kitap_ekle():
     dosya_adi = "kitap.json"
     kitaplar = oku(dosya_adi)

     print("\n Yeni kitap ekleyin:")

     yeni_kitap = {"Barkod": int(input("Barkod Giriniz: ")),
        "Dil": input("Kitap dilini giriniz: "),
        "Fiyat": float(input("Fiyat giriniz: ")),
        "Kitap_Adi": input("Kitap Adını giriniz: "),
        "Yayinevi": input("Yayınevini giriniz: "),
        "Yazar": input("Yazar Adını giriniz: ")  
          }
             
     kitaplar.append(yeni_kitap)

with open("dosya_adi","w", encoding="utf-8") as dosya:  #Listeyi dosyaya kaydettim. json.dump python verisini json "dos." yazdı.
     json.dump(kitaplar, dosya, ensure_ascii=False, indent=4) #kitaplar listesi json a dönüştürülüp dosya içine kaydedildi.
         
print("\n Yeni Kitap Eklendi." )

#kitap arama,isimle

def kitap_ara():
     dosya_adi = "kitap.json"
     kitap_adi = input("Aranacak kitabın adını giriniz: ")

     try:
        with open(dosya_adi, "r", encoding= "utf-8") as dosya:
               kitaplar=json.load(dosya)
     except FileNotFoundError:
        print("Json dosyası bulunmadı.")
        return
     sonuc = [kitap for kitap in kitaplar if kitap["Kitap_Adi"].lower() == kitap_adi.lower()]

     if sonuc : 
          print("\n Bulunan kitap: \n")
          for kitap in sonuc:
            print(f" Kitap Adı: {kitap['Kitap_Adi']}")
            print(f" Yazar: {kitap['Yazar']}")
            print(f" Yayınevi: {kitap['Yayinevi']}")
            print(f" Barkod: {kitap['Barkod']}")
            print(f"  Fiyat: {kitap['Fiyat']} TL")
            print(f"  Dil: {kitap['Dil']}")
            print("-" * 40)
     else:
        print("\nAradığınız kitap bulunamadı.")
     
#kitap silme

def kitap_sil():
    dosya_adi = "kitap.json"

    try:
        barkod = int(input("Silmek istediğiniz kitabın barkod numarasını girin: "))
    except ValueError:
        print("Hata: Geçerli bir barkod numarası girinç")
        return

    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            kitaplar = json.load(dosya)
    except FileNotFoundError:
        print("Hata: kitap.json dosyası bulunamadı!")
        return

    yeni_kitaplar = [kitap for kitap in kitaplar if kitap["Barkod"] != barkod]

    if len(yeni_kitaplar) == len(kitaplar):
        print("\nSilmek istediğiniz kitap bulunamadı.")
        return

    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        json.dump(yeni_kitaplar, dosya, ensure_ascii=False, indent=4)

# uye_islemleri.py

import kitap_islemleri
import json
import os
import zaman
import random

# Üyelerin bilgilerini güncelleyen fonksiyon
def uye_guncelle(uye):
    with open('uye.json', 'r+', encoding='utf-8') as file:
        uyeler = json.load(file)
        for mevcut_uye in uyeler:
            if mevcut_uye['id'] == uye['id']:
                mevcut_uye.update(uye)
                break
        file.seek(0)
        json.dump(uyeler, file, indent=4)
        file.truncate()

# Üyeyi kontrol eden fonksiyon
def uye_kontrol(uye_adi):
    if not os.path.exists('uye.json'):
        return False
    with open('uye.json', 'r', encoding='utf-8') as file:
        uyeler = json.load(file)
        for uye in uyeler:
            if uye['Uye_Adi'] == uye_adi:
                return True
    return False

# Yeni üye ekleyen fonksiyon
def uye_ekle(Uye_Adi, Tel, Adres):
    yeni_uye = {
        'id': str(random.randint(1, 9999)),
        'Uye_Adi': Uye_Adi,
        'Tel': Tel,
        'Adres': Adres
    }
    if os.path.exists('uye.json'):
        with open('uye.json', 'r+', encoding='utf-8') as file:
            uyeler = json.load(file)
            uyeler.append(yeni_uye)
            file.seek(0)
            json.dump(uyeler, file, indent=4)
    else:
        with open('uye.json', 'w', encoding='utf-8') as file:
            json.dump([yeni_uye], file, indent=4)

# Üyeyi arayan fonksiyon
def uye_ara(arama):
    if not os.path.exists('uye.json'):
        return []
    with open('uye.json', 'r', encoding='utf-8') as file:
        uyeler = json.load(file)
        return [uye for uye in uyeler if arama.lower() in uye['Uye_Adi'].lower()]

# Üyeyi silen fonksiyon
def uye_sil(silinecek_uye):
    if not os.path.exists('uye.json'):
        return
    with open('uye.json', 'r+', encoding='utf-8') as file:
        uyeler = json.load(file)
        uyeler = [uye for uye in uyeler if uye['Uye_Adi'] != silinecek_uye]
        file.seek(0)
        json.dump(uyeler, file, indent=4)
        file.truncate()

# Kitap ödünç verme fonksiyonu
def kitap_odunc_verme(Uye_Adi, Kitap_Adi):
    if not uye_kontrol(Uye_Adi):
        print("Üye bulunamadı!")
        return
    tarih = zaman.strftime("%Y-%m-%d")
    odunc_bilgi = {
        'Uye_Adi': Uye_Adi,
        'Kitap_Adi': Kitap_Adi,
        'Tarih': tarih
    }
    takip_yaz(odunc_bilgi)

# Takip dosyasına veri yazan fonksiyon
def takip_yaz(veri):
    if os.path.exists('takip.json'):
        with open('takip.json', 'r+', encoding='utf-8') as file:
            takip = json.load(file)
            takip.append(veri)
            file.seek(0)
            json.dump(takip, file, indent=4)
    else:
        with open('takip.json', 'w', encoding='utf-8') as file:
            json.dump([veri], file, indent=4)

# Takip dosyasından veri okuyan fonksiyon
def takip_oku():
    if not os.path.exists('takip.json'):
        return []
    with open('takip.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Kitap iade eden fonksiyon
def kitap_iade(Uye_Adi, Kitap_Adi):
    takip = takip_oku()
    yeni_takip = [kayit for kayit in takip if not (kayit['Uye_Adi'] == Uye_Adi and kayit['Kitap_Adi'] == Kitap_Adi)]
    with open('takip.json', 'w', encoding='utf-8') as file:
        json.dump(yeni_takip, file, indent=4)

if _name_ == '_main_':
    kitap_odunc_verme("Ali", "Python Programlama")


#  zaman.py
from datetime import datetime, timedelta

def kitap_teslim_suresi_hesapla(alinan_tarih, teslim_suresi_gun):
    """
    Kitap teslim tarihini hesaplar.
    :alinan_tarih: Kitabin alindigi tarih (YYYY-MM-DD)
    :teslim_suresi_gun: Teslim süresi gün olarak
    :return: Teslim tarihi
    """
    alinan_tarih_obj = datetime.strptime(alinan_tarih, "%Y-%m-%d")
    teslim_tarihi = alinan_tarih_obj + timedelta(weeks=2)
    return teslim_tarihi.strftime("%Y-%m-%d")


if _name_ == "_main_":
    alinan_tarih = input("Kitabin alindigi tarihi giriniz (YYYY-MM-DD): ")
    teslim_suresi= 14
    teslim_tarihi = kitap_teslim_suresi_hesapla(alinan_tarih, teslim_suresi)
    print(f"Kitabin alindigi tarih: {alinan_tarih}")
    print(f"Kitabin teslim edilmesi gereken tarih: {teslim_tarihi}")
