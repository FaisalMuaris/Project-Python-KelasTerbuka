import os

if __name__ == "__main__":
    sistem_operasi = os.name

   
    while(True):
        match sistem_operasi:
            case "posix": os.system("clear") #unix / linux
            case "nt": os.system('cls')

        print('SELAMAT DATANG DI PROGRAM')
        print('DATABASE PERPUSTAKAAN')
        print('==========================')

        print(f"1. Read Data")
        print(f"2. Add Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = int(input('Masukan opsi: '))

        print('\n==========================\n')

        match user_option:
            case "1": print('Read Data')
            case "2": print('Add Data')
            case "3": print('Update Data')
            case "4": print('Delete Data')
        
        print('\n==========================\n')
        is_done = input('Apakah Selesai (y/n)')
        if is_done == 'y' or is_done == 'Y':
            break

    print('program berakhir, Terimakasih')