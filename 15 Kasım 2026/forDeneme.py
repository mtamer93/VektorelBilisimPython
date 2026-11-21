#kullanım şekli
# for döngüDegeri in iterableNesne:
    
for a in range(10):
    print("Ankara")

for a in range(1,10):print(a, ". Sayı", sep="")

# (*) işareti başa konursa her elemanı tek tek yazar
print(range(5,10))  
print(*range(5,10))
print(["Elma", "Armut", "Muz"])
print(*["Elma", "Armut", "Muz"])
print(*"Elma")

for item in "Vektörel":
    print(item)

# son harfe gelince sonuna (-) koymaz
sefer = 0
kelime = "Vektörel"
for item in kelime:
    if sefer == len(kelime)-1:
        print(item, end="")
    else:
        print(item, end="-")
        sefer = sefer + 1

print()

# for ile liste yapma
ciftSayilar = [sayi for sayi in range(0,20,2)]
print(ciftSayilar)

print([b*3 for b in "Vektörel"])

print()

# Çarpım tablosu
for a in range(1,11):
    for b in range(1,11):print(f"{a}*{b}={a*b}")
    print()

# Çarpım tablosu
for a in range(1,11):
    for b in range(1,11):
        if a > 5: break     # 5 ten büyükse atlar
        if b % 2 == 0: continue # çift sayıları yazdırmaz
        print(f"{a}*{b}={a*b}")
    print()
