from . import Operasi


def update_console():
    read_console()

    while (True):
        print('Silahkan Pilih Buku yang mau di Upadate')
        no_buku = int(input("Nomer Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print('Nomor Tidak Valid, Silahkan Masukan lagi')
            print("\n"+"="*50)

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        #  Ambil data yang ingin diUpdate
        print('\n'+'='*100)
        print("Silahkan pilih data yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # Memilih Mode Untuk Update
        user_option = input("Pilih data [1,2,3]: ")
        print('\n'+'='*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print(
                                'Tahun Harus Angka, Silahkan Masukan Tahun Lagi (yyyy)')
                    except:
                        print('Tahun Harus Angka, Silahkan Masukan Tahun Lagi (yyyy)')

            case _: print("index tidak cocok")

        print('Data Baru Anda')
        print(f"1. Judul\t: {judul:.40} ")
        print(f"2. Penulis\t: {penulis:.40} ")
        print(f"3. Tahun\t: {tahun:4} ")

        is_done = input('Apakah Selesai (y/n)')
        if is_done == 'y' or is_done == 'Y':
            break

    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)


def create_console():
    print("\n"+"="*100)
    print("Silahkan Tambah Data Buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun Harus Angka, Silahkan Masukan Tahun Lagi (yyyy)')
        except:
            print('Tahun Harus Angka, Silahkan Masukan Tahun Lagi (yyyy)')

# mengambil dari file Operasi dengan fungsi "create"
    Operasi.create(tahun, judul, penulis)
    print("\nBerikut adalah data baru anda")
# Langsung Membaca dari Read_console di file View
    read_console()


def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:2} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-" * 100)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:2} | {judul:.40} | {penulis:.40} | {tahun:4}\n", end="")

    # Footer
    print("="*100 + "\n")
