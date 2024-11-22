class SpesifikasiLaptop:
    def __init__(self, merk, prosesor):
        self.__merk = merk  # Variabel privat
        self._prosesor = prosesor  # Variabel proteksi

    def tampilkan_spesifikasi(self):
        print(f"Merk Laptop: {self.__merk}")
        print(f"Prosesor: {self._prosesor}")

class LaptopGaming(SpesifikasiLaptop):
    def akses_prosesor(self):
        print(f"Prosesor Laptop Gaming: {self._prosesor}")

# Membuat objek dari kelas SpesifikasiLaptop
laptop1 = SpesifikasiLaptop("Asus", "Intel Core i5")
laptop1.tampilkan_spesifikasi()

# Membuat objek dari kelas LaptopGaming
laptop_gaming = LaptopGaming("MSI", "AMD Ryzen 7")
laptop_gaming.akses_prosesor()