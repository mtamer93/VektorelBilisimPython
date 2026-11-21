def topla():
    s1 = int(input("sayi1"))
    s2 = int(input("sayi2"))
    toplam = s1 + s2
    print(f"{s1} ve {s2} sayılarının toplamı {toplam}")

topla()

def topla(a=0, b=0):
    print(f"Sonuc: {a + b}")

topla(5,2)

def toplam(s1 = 0, s2 = 0):
    return s1 + s2

print(toplam(9,5))

c = toplam(11,7)
print(c)


