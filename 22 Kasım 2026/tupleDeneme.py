# Tuple (Degismez dizi)

calismaGunleri = ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma")

print(calismaGunleri)
print(calismaGunleri[1])

# tuple kullanımı
def topla(*sayilar):    # girilen sayilari tuple olarak alir, bu sayilar append veya remove edilemez. (degistirilemez)
    print(sayilar)
    print(type(sayilar))

topla(5,2,8)

