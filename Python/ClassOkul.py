class Okul:
    def __init__(self, adi, turu, kurulusyili, ogretmensayisi, mevcut, sinif_sayisi):
        self.adi = adi
        self.turu = turu
        self.kurulusyili = kurulusyili
        self.ogretmensayisi = ogretmensayisi
        self.mevcut = mevcut
        self.sinif_sayisi = sinif_sayisi


Okul_1 = Okul("İki Eylül", "Orta Okul", 1991, 19, 450, 25)
Okul_2 = Okul("Süleyman Çakır", "Lise", 1981, 34, 650, 35)
Okul_3 = Okul("Anadolu", "Üniversite", 1970, 44, 1450, 45)

Okullar = [Okul_1, Okul_2, Okul_3]

for okul in Okullar:
    print(okul.adi, okul.turu, okul.kurulusyili, okul.ogretmensayisi,
          okul.mevcut, okul.sinif_sayisi)
