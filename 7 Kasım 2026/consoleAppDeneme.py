import random


print("merhaba")

def hesapMakinesi():
    print("\nHESAP MAKINESINE HOSGELDINIZ")
    sayi1 = int(input("Bir sayi girin: "))
    islem = input("Islem giriniz (+,-,*,/): ")
    sayi2 = int(input("Son sayiyi girin: "))

    if islem == '+':
        print(f"Sonuç: {sayi1 + sayi2}")
    elif islem == '-':
        print(f"Sonuç: {sayi1 - sayi2}")
    elif islem == '*':
        print(f"Sonuç: {sayi1 * sayi2}")
    elif islem == '/':
        print(f"Sonuç: {sayi1 / sayi2}")
    else:
        print("Yanlis islem girildi")

def oyun():
    bilgisayar = random.randint(1,10)
    tahmin = 0

    print("\nSAYI TAHMIN OYUNU")
    print("1 ile 10 arasýnda bir sayi tuttum.")

    while tahmin != bilgisayar:
        tahmin = int(input("Tahminin: "))

        if tahmin < bilgisayar:
            print("Daha büyük bir sayi soyle")
        elif tahmin > bilgisayar:
            print("Daha küçük bir sayi soyle")
        else:
            print("Tebrikler! Dogru tahmin ettin!")

def program():
    print("************************************")
    print("*           ANA MENÜ               *")
    print("************************************")
    print("*    1)Hesap Makinesi              *")
    print("*    2)Oyunlar                     *")
    print("*    3)Cikis Yap                   *")
    print("************************************")

    print("Secim Yap")
    secim = input("Secim: ")

    if secim == '1':
        hesapMakinesi()
    elif secim == '2':
        oyun()
    elif secim == '3':
        return False

    return True
        
while program():
    pass
