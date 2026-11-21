#Modulerleştirmek için gereken fonksiyonların tanımlanması

#Bu fonksyion metindeki her bir karakteri alıp ilk önce onluk tabanda
#sonra ikilik tabanda yazdıran ve binary dönüşümünden dolayı karakterin
#başına gelen 0b karakterlerini stringden atıp 0 ile doldurur.
def ascii_tablosu_goster():
    metin = input("Metni Giriniz: ")
    print(f"{'Karakter':<10} | {'Onluk':<10} | {'İkilik':<10}")
    for karakter in metin:
        onluk=ord(karakter)
        binary=bin(onluk)
        print(f"{karakter:<10} | {onluk:<10} | {binary[2:].zfill(8):<10}")

#Bu fonksiyon metindeki her bir karakteri tek tek büyük harf ayrımına
#önem vererek onluk sayı yapıp sonra anahtar kadar arttırıp tekrar
#chara dönüştürüp ayrı bir metine atamaktadır/şifrelemektedir.
#Türkçe karakterler olduğu gibi bırakılır, değiştirilmez.
def sifrele(metin , anahtar):
    sonuc=""
    anahtar=int(anahtar)
    for karakter in metin:
        if 'A' <= karakter <= 'Z':
            onluk=ord(karakter)
            onluk-=65
            onluk+=anahtar
            sifreli=onluk%26
            sifreli+=65
            sonuc+=chr(sifreli)
        elif 'a' <= karakter <= 'z':
            onluk=ord(karakter)
            onluk-=97
            onluk+=anahtar
            sifreli=onluk%26
            sifreli+=97
            sonuc+=chr(sifreli)
        else:
            sonuc+=karakter
    return sonuc

#Bu fonksiyon kendi yazdığımız şifreleme fonksiyonunu, anahtarı
#normalde alınan değerin negatifi olarak kullanarak çağırıp
#kod kirliliğini azaltıp çözümlemektedir.
#Kodu sifrele() fonksiyonundan alındığı için burada da Türkçe
#karakterler değiştirilmez.
def sifre_coz(metin, anahtar):
    anahtar=int(anahtar)
    sonuc=sifrele(metin,-anahtar)
    return sonuc

#Programın Asıl çalıştığı yer
#program başlasın diye döngüyü kıran değer hariç
#bi değer vererek başlatıyoruz
secim = 1
while secim!=0:
    print("===== ASCII & Sezar =====")
    print("1 - ASCII tablosu göster")
    print("2 - Şifrele")
    print("3 - Şifre çöz")
    print("0 - Çıkış")
    secim=int(input("Seçiniz: "))
    match secim:
        case 1:
            ascii_tablosu_goster()
        case 2:
            metin = input("Metni Giriniz: ")
            anahtar = input("Anahtar Giriniz: ")
            sifreliMetin=sifrele(metin,anahtar)
            print(f"Sifreli Metin: {sifreliMetin}")
        case 3:
            metin = input("Sifreli Metni Giriniz: ")
            anahtar = input("Anahtar Giriniz: ")
            cozulmusMetin=sifre_coz(metin,anahtar)
            print(f"Cozulmus Metin: {cozulmusMetin}")
        case 0:
            print("Cikis Yapiliyor! ")
        case _:
            print("Hatali Secim")