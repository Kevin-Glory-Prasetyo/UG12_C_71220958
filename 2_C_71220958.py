
baris = input("masukan angka : ")

angka = input("masukan angka yang dihitung : ")

jumlah = 0

for i in range(len(baris)):

    if baris[i] == angka:
        jumlah += 1

print("angka {} mucul sebanyak {}kali".format(angka, jumlah))