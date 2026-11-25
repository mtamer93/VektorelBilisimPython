class Ogrenci():
    ad = "--"
    nu = 0
    def __str__(self): return f"Öğrenci adı: {self.ad}, öğreci numarası: {self.nu}"

ogrenci1 = Ogrenci()
ogrenci1.ad = "Semih"
ogrenci1.nu = 222

print(ogrenci1)
        