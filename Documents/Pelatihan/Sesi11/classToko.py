class Toko:
    lstAll = [{"name": "Gula", "harga": 13000},
              {"name": "Kopi", "harga": 27000},
              {"name": "Beras", "harga": 11000},
              {"name": "Kecap", "harga": 20000},
              {"name": "Saus", "harga": 25000},
              {"name": "Terigu", "harga": 22000},
              {"name": "Tapioka", "harga": 18000},
              {"name": "Telur", "harga": 23000}
              ]

    def __init__(self):
        self.item = []
        self.harga = 0

    def getTotalPrice(self, jumlah):
        return float(self.harga) * jumlah

    def listHarga(self):
        print("---------------------------")
        print("Selamat datang di Toko kami")
        print("Silahkan Pilih Pesanan Anda:")
        print("1. Gula     Rp. 13.000,-/kg")
        print("2. Kopi     Rp. 27.000,-/kg")
        print("3. Beras    Rp. 11.000,-/kg")
        print("4. Kecap    Rp. 20.000,-/kg")
        print("5. Saus     Rp. 25.000,-/kg")
        print("6. Terigu   Rp. 22.000,-/kg")
        print("7. Tapioka  Rp. 18.000,-/kg")
        print("8. Telur    Rp. 23.000,-/kg")
        print("Masukkan Pesanan")

    def pilihan(self):
        item = int(input("Pilih Item nomer: "))
        if item > 8:
            print("maaf pilihan tidak tersedia.")
            self.pilihan()
        else:
            nama = self.lstAll[item - 1]
            print("Anda memilih " + nama["name"] + " dengan Harga Rp. " + str(nama["harga"]))
            banyak = int(input("Berapa banyak: "))
            total = banyak * nama["harga"]
            self.harga += total
            print(total)
            self.item.append(nama["name"] + " x " + str(banyak) + " Rp. " + str(total))
            print("Apakah anda Masih Mau belanja")
            print("0. Sudah cukup")
            print("1. Masih")
            self.lanjut()


    def lanjut(self):
        pilihan = int(input("Pilihan : "))
        if pilihan == 0:
            print("Pilihan selesai")

        elif pilihan == 1:
            self.pilihan()

        else:
            print("Pilihan tidak tersedia")
            self.lanjut()

    def getListBelanjaan(self):
        for i in self.item:
            print(i)
        print("Total Harga Rp. " + str(self.harga))

    def getCashBack(self):
        uang = int(input("Masukkan Uang Anda: "))
        kembalian = uang - self.harga
        # print(kembalian)
        if uang < self.harga:
            print("Uang Anda Kurang")
        elif uang >= self.harga:
            print("Uang kembalian Anda Rp. " + str(kembalian))

    def result(self):
        self.listHarga()
        self.pilihan()
        self.getListBelanjaan()
        self.getCashBack()

toko = Toko()
toko.result()













