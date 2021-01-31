'''
---------------------------
Sending E-Mail using Python
---------------------------
Indonesia.ai Final Project
Basic Python - Batch 03 / Team B / Group 2
'''

'''Library yang dibutuhkan'''
import smtplib, ssl #membuat koneksi yang aman dengn SMTP server Gmail
import getpass #hide passsword
import os #untuk clear screen
#Multipurpose Internet Mail Extensions (MIME)
#Berguna untuk membangun struktur email dari awal *Scratch message structure
from email.mime.text import MIMEText #untuk handling text
from email.mime.multipart import MIMEMultipart #untuk beberapa data
from email.mime.base import MIMEBase 
from email import encoders #untuk Content-Transfer-Encoding  

os.system('cls') #System Clear Screen

'''Function for Email Content'''
#Read Only Document - Isi Email
emailBody = open(r"D:\Training\basic_python\Final-Project\email_content.txt", "r") 
#open(r'path') untuk Raw data agar interpretasi backslash tidak menjadi Escape Sequence seperti \n \r
isiEmail = emailBody.readlines()
emailBody.close()
def emailSbj() : #Function Subject Email
    for x in isiEmail[1:2] :
        judulEmail=x
    return judulEmail
def emailContent() : #Function Isi Pesan
    ctEmail=[] #List Preparation
    barisEmail=''
    for y in isiEmail[3:] :
        ctEmail.append(y)
    #return ctEmail  
    return (barisEmail.join(ctEmail)) #Gabungkan list menjad text

#Read Only Document - Penerima Email      
emailRecepient = open(r"D:\Training\basic_python\Final-Project\email_receiver.txt", "r")
rcpEmail = emailRecepient.readlines()
emailRecepient.close()
penerima= [] #preparation empty list
i=0
while i < len(rcpEmail) :
    penerima.append(rcpEmail[i].strip()) #strip untuk hapus \n (Linefeed)
    i +=1
    #output akan seperti ['fulan1@email.com','fulan2@email.com' dst]

'''E-Mail Processing'''
#Initial Setup
def SMTPopt(emailDom) :
    if emailDom == 'yahoo.com':
        smtp_server="smtp.mail.yahoo.com" #SMTP Server Gmail
    elif emailDom == 'gmail.com':
        smtp_server="smtp.gmail.com" #SMTP Server Gmail
    return smtp_server

port = 465 #untuk SSL port 
emailPenerima= penerima #multiple receiver dengan list

'''[Program] Input Data Email'''
try :
    print('Masukan E-mail & Password anda :')
    print('--------------------------------')
    emailPengirim=input('Masukan email : ')
    password = getpass.getpass('Masukan password : ')
    confirmAttachment=input('Kirim dengan file [Y/N] : ')
    if confirmAttachment == 'Y' :
        uploadFile=input('Masukan path file lengkap : ')
    else :
        uploadFile= None         
    #Proses inisiasi email
    fnEmail=emailPengirim.rfind("@")
    emailDn=emailPengirim[fnEmail+1:]
except Exception as error:
    print("Terjadi Kesalahan")
else :
    print("\n")
    print("Harap tunggu, program sedang melakukan pengiriman.......")

'''E-Mail Content'''
psnEmail = MIMEMultipart()
psnEmail["Subject"] = emailSbj() #calling function
psnEmail["From"] = emailPengirim
psnEmail["To"] = ", ".join(emailPenerima)
text = emailContent() #calling function
psnEmail.attach(MIMEText(text, 'plain')) #adding text to body email

if uploadFile is not None :
    #Attachment
    pathLoc = r"{}".format(uploadFile) #convert ke raw
    atchFile = MIMEBase('application', "octet-stream") #berubah menjadi data biner dalam format bebas
    atchFile.set_payload(open(pathLoc, "rb").read()) #rb translation non-text file
    encoders.encode_base64(atchFile) #encoding ke base64 - biner menjadi teks
    #Read file name & Type
    paths = repr(pathLoc) #mengembalikan representasi object
    postNm=paths.rfind("\\")+1  #mencari backslash dari kanan
    atchName=str(paths[postNm:].replace("'",""))    
    atchFile.add_header('Content-Disposition', 'attachment', filename=atchName)
    psnEmail.attach(atchFile)

'''Process Pengiriman Email'''
context = ssl.create_default_context() #membuat ssl context yang paling highly recommended
with smtplib.SMTP_SSL(SMTPopt(emailDn), port, context=context) as emailServer :
    try :
        #Proses login
        emailServer.login(emailPengirim, password)
        #Pengiriman email disini
        emailServer.sendmail(emailPengirim, emailPenerima,psnEmail.as_string()) 
        emailServer.quit() #koneksi akan secara otomatis close saat program selesai dieksesusi
    except Exception as error:
        print("Maaf, program gagal mengirim email :(")
    else :
        os.system('cls')
        totalRecpt = len(rcpEmail)
        print("E-Mail Telah Terkirim ke-", totalRecpt, "penerima!")
        print("-------------------------------------")
        i=0
        while i < totalRecpt :
            print(rcpEmail[i].strip())
            i +=1
        print("-------------------------------------")
        print('\n')