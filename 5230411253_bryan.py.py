class daftar_menu:
    def menumakan():
        print("=====menu makanan=====")
        print("1. Bakso (15.000)")
        print("2. mie ayam (10.000)")
        print("3.  ramen (20.000)")
        print("4. sushi (50.000)")

def struk(A,B,C,D,E):
        import datetime
        print("")
        print("==================")
        print("======Struk=======")
        print(f"===Nama      : {B}")
        print("===Beli      :")
        for item in A:
            print(f"              - {item}")
        print(f"===Tagihan   : Rp.{C}")
        print(f"===Uang      : Rp.{D}")
        print(f"===Kembalian : Rp.{E}")
        print(f"===Waktu Pemesanan: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        print("==================")

while True:
    nama = input("Masukan nama anda: ")
    THarga = 0
    Belanjaan = []
    while True:
        daftar_menu()
        Menu = int(input("Pilih menu (1-4) atau (0) untuk mengakhiri pembelian : "))
        if Menu == 0:
            break
        if Menu in [1, 2, 3, 4]:
            menu_harga = {
                1: ('bakso', 15.000),
                2: ('mie ayam', 10.000),
                3: ('ramen', 20.000),
                4: ('sushi', 50.000)
            }
            if Menu in menu_harga:
                menu, harga = menu_harga[Menu]
                inputJumlah_makan = int(input("Masukkan jumlah makanan : "))
                subtotal = harga * inputJumlah_makan
                THarga += subtotal
                Belanjaan.append(f"{inputJumlah_makan} {menu} (Rp.{subtotal})")
            else:
                print("Menu tidak valid, silakan pilih kembali.")
        else:
            print("Masukan tidak valid, silakan masukkan angka (1-4) atau (0).")
    uang = int(input("Masukkan jumlah uang yang diberikan: "))
    kembalian = uang - THarga
    struk(Belanjaan,nama,THarga,uang,kembalian)
    lanjut = input("Apakah ada pelanggan berikutnya? (ya/tidak) ")
    if lanjut.lower() != 'ya':
        break

def menuminum():
        print("=====menu minuman=====")
        print("5. es teh (5.000)")
        print("6. es jeruk (6.000)")
        print("7. jus alpukat (10.000)")
        print("8. air mineral (3.000)")

def struk(f,g,h,i,j):
        import datetime
        print("")
        print("==================")
        print("======Struk=======")
        print(f"===Nama      : {g}")
        print("===Beli      :")
        for item in f:
            print(f"              - {item}")
        print(f"===Tagihan   : Rp.{h}")
        print(f"===Uang      : Rp.{i}")
        print(f"===Kembalian : Rp.{j}")
        print(f"===Waktu Pemesanan: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        print("==================")

while True:
    nama = input("Masukan nama anda: ")
    THarga = 0
    Belanjaan = []
    while True:
        daftar_menu()
        Menu = int(input("Pilih menu (5-8) atau (0) untuk mengakhiri pembelian : "))
        if Menu == 0:
            break
        if Menu in [5, 6, 7, 8]:
            menu_harga = {
                5: ('es teh', 5.000),
                6: ('es jeruk', 6.000),
                7: ('jus alpukat', 10.000),
                8: ('air mineral', 3.000)
            }
            if Menu in menu_harga:
                menu, harga = menu_harga[Menu]
                inputJumlah_minuman = int(input("Masukkan jumlah minuman : "))
                subtotal = harga * inputJumlah_minuman
                THarga += subtotal
                Belanjaan.append(f"{inputJumlah_minuman} {menu} (Rp.{subtotal})")
            else:
                print("Menu tidak valid, silakan pilih kembali.")
        else:
            print("Masukan tidak valid, silakan masukkan angka (5-8) atau (0).")
    uang = int(input("Masukkan jumlah uang yang diberikan: "))
    kembalian = uang - THarga
    struk(Belanjaan,nama,THarga,uang,kembalian)
    lanjut = input("Apakah ada pelanggan berikutnya? (ya/tidak) ")
    if lanjut.lower() != 'ya':
        break