# while kullanimi
# while mantiksal_ifade:
#   calisacak komutlar
#   calisacak komutlar
#   ...

a = 5   
while a < 10:   # ifade dogru (True) oldugu sürece while calisir. a nın 10 dan kücük oldugu durumlarda calisir.
    print(a)
    a += 1

# enter a basildigi müddetce rastgele sayilar yazan program
import random
devam = ""
while devam == "":
    print(random.randint(1,1000))
    devam = input("Devam etmek için enter a basın.")

# Çekiliş programı (öğrenci ekleme, öğrenci silme, rastgele bir öğrenci seçme)
ogranciler = ["Burak", "Yagiz", "Necati"]
def listele():
    print("Cekilise katilacak ogrenciler:")
    for isim in ogranciler: print(isim, end=", ")
    print()

def ekle():
    while True:
        ogrenci = input("Eklenecek öğrenci (Baska ogrenci yoksa enter a bas): ")
        if ogrenci == "": break
        else: ogranciler.append(ogrenci)
    listele()

def sil():
    while True:
        ogrenci = input("Silinecek öğrenci (Baska ogrenci yoksa enter a bas): ")
        if ogrenci == "": break
        else: ogranciler.remove(ogrenci)
    listele()

def sec():
    print("Sansli ogrencimiz: ", random.choice(ogranciler))

def menu():
    listele()
    print("Çekiliş Programı")
    print("1-Öğrenci Ekle")
    print("2-Öğrenci Cikar")
    print("3-Öğrenci Sec")
    print("4-Cikis")
    secim = input()

    if secim == '1':
        ekle()
    if secim == '2':
        sil()
    if secim == '3':
        sec()
    if secim  == '4':
        exit()
    menu()

menu()

    