class Personel:
    def __init__(self, adi, departmani, calisma_yili, maasi):
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maasi = maasi

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adi:", personel.adi)
            print("Departmani:", personel.departmani)
            print("Calisma Yili:", personel.calisma_yili)
            print("Maasi:", personel.maasi)
            print("-----------------------------")

    def maas_zammi(self, personel, zam_orani):
        personel.maasi *= (1 + zam_orani / 100)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)

# Örnek kullanım:
if __name__ == "__main__":
    personel1 = Personel("Ahmet", "Bilgi Islem", 5, 5000)
    personel2 = Personel("Mehmet", "Insan Kaynaklari", 3, 4500)

    firma = Firma()
    firma.personel_ekle(personel1)
    firma.personel_ekle(personel2)

    print("Firma Personelleri:")
    firma.personel_listele()

    firma.maas_zammi(personel1, 10)
    print("Ahmet'in maasi arttirildi.")

    print("Guncel Firma Personelleri:")
    firma.personel_listele()

    firma.personel_cikart(personel2)
    print("Mehmet firmadan cikarildi.")

    print("Guncel Firma Personelleri:")
    firma.personel_listele()
