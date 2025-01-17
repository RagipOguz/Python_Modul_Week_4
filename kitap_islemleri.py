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
        json.dump(yeni_kitaplar, dosya, ensure_ascii=False, indent=4)


