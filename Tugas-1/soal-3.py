#Input Nilai
nilaiTeori = float(input("Masukan nilai ujian teori :"))
nilaiPraktek = float(input("Masukan nilai ujian praktek :"))
#Branching
if nilaiTeori>=70.0 and nilaiPraktek>=70.0 :
    print('Selamat, anda Lulus!')
elif nilaiTeori>=70.0 and nilaiPraktek<70.0 :
    print('Anda harus mengulang ujian praktek.')
elif nilaiTeori<70.0 and nilaiPraktek>=70.0 :
    print('Anda harus mengulang ujian teori.')   
else :
     print('Anda harus mengulang ujian teori dan praktek.')