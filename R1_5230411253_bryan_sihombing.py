
class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat


class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk


class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Snack")
        self.harga = harga


class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Makanan")
        self.harga = harga


class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Minuman")
        self.harga = harga


class Transaksi:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.detail_transaksi = []  

    def tambah_detail(self, produk, jumlah):
        self.detail_transaksi.append((produk, jumlah))

    def hapus_detail(self, kode_produk):
        
        self.detail_transaksi = [
            (produk, jumlah) for produk, jumlah in self.detail_transaksi if produk.kode_produk != kode_produk
        ]

    def total_harga(self):
        return sum(produk.harga * jumlah for produk, jumlah in self.detail_transaksi)


class Struk:
    def __init__(self, transaksi):
        self.transaksi = transaksi

    def cetak_struk(self):
        print(f"No Transaksi: {self.transaksi.no_transaksi}")
        print(f"Nama Pegawai: {self.transaksi.pegawai.nama}")
        print("Daftar Produk:")
        for produk, jumlah in self.transaksi.detail_transaksi:
            print(f" - {produk.nama_produk} (Jenis: {produk.jenis_produk}) x{jumlah} = {produk.harga * jumlah}")
        print(f"Total Harga: {self.transaksi.total_harga()}\n")


pegawai1 = Pegawai("123456", "Budi", "Jl. Merdeka No.1")
pegawai2 = Pegawai("789012", "Siti", "Jl. Sudirman No.5")
pegawai3 = Pegawai("345678", "Rudi", "Jl. Gatot Subroto No.10")


snack1 = Snack("S001", "Chips", 10000)
snack2 = Snack("S002", "Chocolate", 15000)
makanan1 = Makanan("M001", "Nasi Goreng", 20000)
makanan2 = Makanan("M002", "Mie Goreng", 18000)
minuman1 = Minuman("D001", "Teh Botol", 5000)
minuman2 = Minuman("D002", "Kopi", 12000)


transaksi1 = Transaksi("T001", pegawai1)
transaksi1.tambah_detail(snack1, 2)
transaksi1.tambah_detail(makanan1, 1)
transaksi1.tambah_detail(minuman1, 3)


transaksi2 = Transaksi("T002", pegawai2)
transaksi2.tambah_detail(snack2, 1)
transaksi2.tambah_detail(makanan2, 2)
transaksi2.tambah_detail(minuman2, 1)


print("=== Struk Sebelum Penghapusan ===")
struk1 = Struk(transaksi1)
struk1.cetak_struk()

struk2 = Struk(transaksi2)
struk2.cetak_struk()


transaksi1.hapus_detail("M001")


print("=== Struk Setelah Penghapusan ===")
struk1.cetak_struk()
