a = 5               # int tipinde
sehir = "Ankara"    # str tipinde
fiyat = 80.5        # float tipinde
kayitliMi = True    # boolean tipinde True ya da False ( 1 bitlik yer kaplar )

# type ile arkaplanda belirlenen tipleri gorebiliriz
print(a, type(a))
print(sehir, type(sehir))
print(fiyat, type(fiyat))
print(kayitliMi, type(kayitliMi))

ogrenciler = []     # list = liste = dizi = collection. Pythonda 4 cesit collection vardir.
ogrenciler = ["Burak", "Necati", "Yagiz"]

print(ogrenciler, type(ogrenciler))

s = "54"
sss = int(s)

veri1 = str(a)
veri2 = float(a)

print(s, type(s))
print(sss, type(sss))
print(veri1, type(veri1))
print(veri2, type(veri2))

# global ve local
# pythonda en sola dayali alandaki kodlar global alandaki kodlar olur.
# fonksiyon, sinif vb yapilar ise local alan olur
sayac = 5
def arttir():
    global sayac
    sayac += 2

arttir()
print(sayac)