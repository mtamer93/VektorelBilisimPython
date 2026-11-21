if True:
    print("Selam")

if False:
    print("Merhaba")

if 3 < 5: print("Ankara")
else: print("aaa")

if 13 < 5: print("İstanbul")
else: print("bbb")

ortalama = 60

if ortalama > 90 and ortalama < 100: print("Süper")
elif ortalama > 70 and ortalama < 100: print("Çok iyi")
elif ortalama > 49 and ortalama < 100: print("Geçtin")
elif ortalama <= 49 and ortalama >= 0: print("Kaldın")
else: print("Yanlış giriş")

ortalama = 49

print("Kaldın" if ortalama < 50 else "Geçtin") # ternary if kullanımı
