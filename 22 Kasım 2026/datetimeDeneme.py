import datetime as dt
import time as t

print(dt.datetime.now())    # suanki tarihi ve saati yazar.

# strftime ile tarihi formatli yazmak:
# %d Gün
# %m Ay
# %Y 4 basamaklı yıl
# %y 2 basamaklı yıl
# %H Saat (24 saat)
# %I Saat (12 saat)
# %M Dakika
# %S Saniye
# %A Günün tam adı
# %B Ayın tam adı
# istenilen tarihi strftime ile istedigimiz formatta yazabiliriz. Sadece gün, ay, yil, saat, dakika vb.
print(dt.datetime.now().strftime("%d %B %A %H:%M"))   # %d : Gün, %B : Ayin tam adi, %A : Günün tam adi, %H : Saat, %M : Dakika

print(dt.datetime.now().year)   # sadece suanki yili yazar.
print(dt.datetime.now().month)   # sadece suanki ayi yazar.
print(dt.datetime.now().day)   # sadece suanki günü yazar.

print(dt.datetime.now().hour)   # sadece suanki saati yazar.
print(dt.datetime.now().minute)   # sadece suanki dakikayi yazar.

t.sleep(3)  # icine yazilan saniye kadar bekler.
print("3 saniye geçti")