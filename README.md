# ASCII Dönüştürücü ve Sezar Şifreleme/Çözme Konsolu

## Öğrenci Bilgileri
- Ad Soyad: Heysen Şengül
- Öğrenci No: 25360859064
- Ders: BLM101 Bilgisayar Mühendisliğine Giriş

## Proje Hakkında
Program kullanıcıdan aldığı metindeki harfleri onluk ve ikili sistemde yazıp kullanıcıya verebilmekte,metini verdiğiniz bir anahtar sayıya  göre şifreleyip, şifreli metinleride anahtar bilinirse çözebilmektedir.

## Nasıl Çalıştırılır
- Gereken Python sürümü: 3.10 veya üstü
- Komut: python src/main.py

## Menü Seçenekleri
1. ASCII tablosu göster
2. Şifrele
3. Şifre çöz
0. Cikis

## Fonksiyonlar
### ascii_tablosu_goster()
Bu fonksyion metindeki her bir karakteri alıp ilk önce onluk tabanda sonra ikilik tabanda yazdıran ve binary dönüşümünden dolayı karakterin başına gelen 0b karakterlerini stringden atıp 0 ile doldurur.
### sifrele(metin, anahtar)
Bu fonksiyon metindeki her bir karakteri tek tek büyük harf ayrımına önem vererek onluk sayı yapıp sonra anahtar kadar arttırıp tekrar chara dönüştürüp ayrı bir metine atamaktadır/şifrelemektedir. Türkçe karakterler olduğu gibi bırakılır, değiştirilmez.
### sifre_coz(metin, anahtar)
Bu fonksiyon kendi yazdığımız şifreleme fonksiyonunu, anahtarı normalde alınan değerin negatifi olarak kullanarak çağırıp kod kirliliğini azaltıp çözümlemektedir. Kodu sifrele() fonksiyonundan alındığı için burada da Türkçe karakterler değiştirilmez.

## Algoritmanın Mantığı
Pythonun içine gömülü fonksiyonları kullanarak metindeki karakterleri onluk sisteme geçirip(ASCII tablosundaki yerlerini bulup)  bunu alfabadeki sisteme(0-26 arasına) döndürüp(65 çıkarma) sonrasında da şifrelememizi sağlayacak anahtar ile toplayıp tekrardan ASCII tablosunda döndürerek(65 ekleyerek) çıktıya ekliyoruz.Çözüm içinde tam tersi geçerlidir.

## Notlar
Türkçe karakterler diğer karakterlere göre ASCII tablosunda farklı yerlerde bulunduğu için fonksiyonlarımızın matematiksel hesaplamaların dışında kalmakta ve şifrenin kırılması açısından daha zor olduğunu düşünmekteyim.  

## Örnek Çalıştırma
```
===== ASCII & Sezar =====
1 - ASCII tablosu göster
2 - Şifrele
3 - Şifre çöz
0 - Çıkış
Seçiniz: 1
Metni Giriniz: Ahmet
Karakter   | Onluk      | İkilik    
A          | 65         | 01000001  
h          | 104        | 01101000  
m          | 109        | 01101101  
e          | 101        | 01100101  
t          | 116        | 01110100  
===== ASCII & Sezar =====
1 - ASCII tablosu göster
2 - Şifrele
3 - Şifre çöz
0 - Çıkış
Seçiniz: 2
Metni Giriniz: Merhaba, Dünya!
Anahtar Giriniz: 6
Sifreli Metin: Skxnghg, Jüteg!
===== ASCII & Sezar =====
1 - ASCII tablosu göster
2 - Şifrele
3 - Şifre çöz
0 - Çıkış
Seçiniz: 3
Sifreli Metni Giriniz: Skxnghg, Jüteg!
Anahtar Giriniz: 6
Cozulmus Metin: Merhaba, Dünya!
===== ASCII & Sezar =====
1 - ASCII tablosu göster
2 - Şifrele
3 - Şifre çöz
0 - Çıkış
Seçiniz: 0
Cikis Yapiliyor!
```
