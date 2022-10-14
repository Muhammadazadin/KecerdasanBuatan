

def penghasilan():
    print('================================')
    print('Muhammad Azadin Noor            ')
    print('20009106129                     ')
    print('klasifkasi tingkatan pekerjaan  ')
    print('Berdasarkan Penghasilan         ')
    print('================================')
    
    rupiah = int(input("Inputkan Gaji anda: "))
    if rupiah >= 10000000 :
       grade = "investor"
    elif rupiah >= 5000000  :
       grade = "Ceo"
    elif rupiah >= 1000000 :
       grade = "Pekerja"
    elif rupiah >= 500000 :
       grade = "Freelence"
    elif rupiah >= 100000 :
       grade = "Mahasiswa"
    else:
       grade = "Pengangguran"
    
    print("Grade: %s" % grade)
    mengulang = input('apakah ingin mengulang(y/t): ')
    if mengulang  == 'y':
        penghasilan()
    elif mengulang == 't':
        print('please enter...')

penghasilan()



