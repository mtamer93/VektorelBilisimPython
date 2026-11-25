# dict

# elemanları key-value ikilisinden oluşur. index yerine key kullanılır.

tr_en_sozluk = {

    "köpek" : "dog",
    "kedi" : "cat",
    "fil" : "elephant"
}

print(tr_en_sozluk)
print(tr_en_sozluk.keys())
print(tr_en_sozluk.values())

kelime = input("Cevrilecek kelimeyi gir:")
if kelime in tr_en_sozluk.keys():print(kelime, "kelimesinin İngilizce'si:", tr_en_sozluk[kelime])   # kelime sozlukte varsa value sunu gosterir.
else: print("Bu kelime sözlükte yok.")

# ilanlar programi
ilan1 = {"adi":"acil satilik ev", "fiyatı" : 5000000}
ilan2 = {"adi":"ogretmenden satilik clio", "fiyatı" : 300000}
ilan3 = {"adi":"sifir ayarinda notebook", "fiyatı" : 10000}
ilanlar = {
    "254" : ilan1,
    "568" : ilan2,
    "587" : ilan3
}

print(ilanlar)
print(ilanlar["568"])
print(ilanlar["568"]["fiyatı"])