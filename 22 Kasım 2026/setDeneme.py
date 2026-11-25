# Set (index vb adresleme yoktur.)

yetkiler = {"Öğretmen", "İdareci", "Öğrenci"}

print(yetkiler)
print(type(yetkiler))

# eleman ekleme
yetkiler.add("Veli")
print(yetkiler)

# eleman silme
yetkiler.remove("Veli")
print(yetkiler)

# yeni bir setle birleştirmek için
yeniYetkiler = {"Memur", "Doktor", "Yönetici"}
yetkiler.update(yeniYetkiler)
print(yetkiler)

# sette index yoktur. Elemanın var olup olmadığı önemlidir.
print("Öğretmen" in yetkiler)   # True çünkü sette bu eleman var.