skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

harga_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]

ongkos_kirim = 12000
total_pengeluaran = ongkos_kirim + skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6

rata_rata = total_pengeluaran / len(harga_skincare)

nim = 54

konversi_JPY = total_pengeluaran / 113

isi_skincare_3_sampai_5 = harga_skincare[-4:-1]

bolean = nim < rata_rata

print("skincare_1 =", skincare_1)
print("skincare_2 =", skincare_2)
print("skincare_3 =", skincare_3)
print("skincare_4 =", skincare_4)
print("skincare_5 =", skincare_5)
print("skincare_6 =", skincare_6)
print("harga skincare =", harga_skincare)
print("ongkos kirim =", ongkos_kirim)
print("total pengeluaran =", total_pengeluaran)
print("rata-rata =", rata_rata)
print("nim =", nim)
print("bolean =", bolean)
print("total pengeluaran dalam mata uang Yen Jepang =", konversi_JPY)
print("harga skincare 3 sampai skincare 5=", isi_skincare_3_sampai_5)
#horeee slesai :)