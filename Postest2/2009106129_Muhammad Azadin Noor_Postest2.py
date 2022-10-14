import pandas as pd
print('================================')
print('Muhammad Azadin Noor            ')
print('20009106129                     ')
print('klasifkasi tingkatan pekerjaan  ')
print('Berdasarkan Penghasilan         ')
print('================================')
    
data = {"Nama": ["Gilang","azadin","cuan","rahmad","rojak","Budi","Yuda","la boy","anto","arya","Tiko","zaenal","udin","joko","Berli"],
                 "Penghasilan": [10000000,9000000,11000000,4000000,5000000,6000000,5000000,7000000,5500000,500000,550000,600000,445000,700000,500000],
                 "status":["investor","investor","investor","Pekerja","Pekerja","Pekerja","Pekerja","Pekerja","Pekerja","Mahasiswa","Mahasiswa","Mahasiswa","Mahasiswa","Mahasiswa","Mahasiswa"]
            }
df = pd.DataFrame(data)
df.to_csv("dataklasifikasi.csv")
print(df)
