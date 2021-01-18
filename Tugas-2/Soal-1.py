'''
Program Input Nama & No Telepon
/Input telepon tanpa validasi berupa angka - bebas input/
'''
#Library untuk clear screen (cls)
import os

#Function yang dibutuhkan
def cls(): #clear screen
    os.system('cls')

def listContact(): #menampilkan list contact
    if len(contact) < 1 :
        print("Kontak masih kososng")
    else :
        print("Daftar Contact")
        print("--------------")
        for i in contact : #akses dict
            for key,value in i.items():
                print('Nama :' + key)
                print('No Telepon::', value)

def addContact(nama,notlp): #insert data
    if len(nama) > 0 and len(notlp) > 0 :
        contactList=dict() #preparation dict
        contactList[nama] = notlp #key & value
        contact.append(contactList) #insert
        print('Contact berhasil ditambahkan')
    else :
        print('Data yang anda masukan tidak lengkap')

def out(): #close program
    print('Program selesai, sampai jumpa!')

def errors(): #error Input
    print('Menu Tidak Tersedia')

#Preparation
contact=[] #Empty list untuk menampung semua data dalam satu list
stsProgram = 1 #looping status

#Looping Program
while stsProgram == 1 : #infinity loop
    print('Selamat Datang!')
    print('------Menu------')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    action = input("Masukan Perintah :")
    perintah = int(action)

    #Ifelse condition
    if perintah == 1:
        listContact()
        goTask = input("")
        cls()   
    elif perintah == 2 :
        name = input("Masukan Nama  :")
        notlp = input("Masukan No Telepon :")
        addContact(name,notlp)
        goTask = input("")
        cls()   
    elif perintah == 3 :
        out()
        stsProgram = 0 #Program Off
        goTask = input("")
        cls()    
    else:
        errors()
        goTask = input("")   
        cls() 






