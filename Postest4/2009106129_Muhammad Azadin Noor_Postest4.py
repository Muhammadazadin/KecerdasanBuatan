import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

metode = input('Pilih(1/2/3)  ')
if metode == '1':
    print(df)
elif metode == '2':
    population_mhs = [1,2,3,4,5]
    penghasilan = [500000,700000,1000000]
    plt.hist(population_mhs, penghasilan, histtype='bar', rwidth=0.5)
    plt.xlabel('penghasilan')
    plt.ylabel('Data penghasilan')
    plt.title('Data Bulan KE 1')
    plt.show()
elif metode == '3':
    x = np.arange(1,7) 
    y = 2 * x + 5 
    plt.title("Data PER 6 Bulan") 
    plt.xlabel("kenaikan penghasilan") 
    plt.ylabel("Data per 6 bulan") 
    plt.plot(x,y) 
    plt.show()