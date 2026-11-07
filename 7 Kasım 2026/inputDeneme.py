# Klavyeden girilen 2 sayıyı toplayan program
# Kullanıcıdan klavye ile bilgi almak için input fonksiyonu kullanılır.
# input fonksiyonu bilgiyi string olarak alır.

sayi1 = input("1. sayıyı giriniz:")
sayi2 = input("2. sayıyı giriniz:")

toplam = sayi1 + sayi2

print(f"{sayi1} + {sayi2} = {toplam}")  # string olarak toplar yani yan yana yazar

sayi1 = int(sayi1)
sayi2 = int(sayi2)

toplam = sayi1 + sayi2

print(f"{sayi1} + {sayi2} = {toplam}") # doğru işlem yapar çünkü sayilari int e çevirdik.

#input
ad = input("Adınız nedir? ")
dy = int(input(f"hangi yılda doğdun {ad}: "))
print(f"Demek {2026-dy} yaşındasın {ad}.")

#if şart belirtir, if şart : yazılır alt satırlar girintili yazılır.

secim = input("İşleminiz nedir?\n(Toplamak için +, çıkartmak için -, çarpmak için *, bölmek için /): ")

if secim == '+':
    print(f"Sonuç: {sayi1 + sayi2}")
if secim == '-':
    print(f"Sonuç: {sayi1 - sayi2}")
if secim == '*':
    print(f"Sonuç: {sayi1 * sayi2}")
if secim == '/':
    print(f"Sonuç: {sayi1 / sayi2}")

input()
