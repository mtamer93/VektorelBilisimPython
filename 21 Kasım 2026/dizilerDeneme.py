print("Merhaba")

# 50 den 100 e kadar olan tüm cift sayilardan olusan bir dizi olusturur.
ellidenYuzeCiftSayilar = []
for i in range(50,101):
    if i%2 == 0:
        ellidenYuzeCiftSayilar.append(i)

print(ellidenYuzeCiftSayilar)

# Pythonda dizilere collection denir. 
# Pythonda 4 tur collection vardir.
# 1- list / liste : esnek collection
# 2- tuple / demet : degismez collection
# 3- set / kume : index vb adresleme yoktur
# 4- dict / dictionary / sozluk : elemanlari key-value ikilisinden olusur. Index yerine key kullanilir.

# Liste islemleri
ogrenciler = ["Burak", "Necati", "Yagiz"]
# liste degerlerine ulasmak
print(ogrenciler)
print(ogrenciler[1])

# listeye eleman eklemek
ogrenciler.append("Nihat")
print(ogrenciler)

ogrenciler.insert(1,"Metehan") # insert araya eleman eklemek icin kullanilir.
print(ogrenciler)

ogrenciler.remove("Yagiz") # remove eleman siler
print(ogrenciler)

ogrenciler.pop() # en son elemani siler
print(ogrenciler)

ogrenciler.pop(1) # 1 indexli elemani siler
print(ogrenciler)

ogrenciler = ['Burak', 'Metehan', 'Necati', 'Yagiz', 'Nihat']
print(ogrenciler)

print(ogrenciler[2:]) # 2 indexli elemandan sona kadar yazar
print(ogrenciler[:2]) # bastan 2 indexli elemana kadar yazar
print(ogrenciler[1:3]) # 1 indexli den 3 indexine kadar olan elemanlari yazar