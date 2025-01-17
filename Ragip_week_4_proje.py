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
