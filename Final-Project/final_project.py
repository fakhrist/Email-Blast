'''
---------------------------
Sending E-Mail using Python
---------------------------
Indonesia.ai Final Project
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
def emailSbj() :
    #Subject Email
    for x in isiEmail[1:2] :
        judulEmail=x
    return judulEmail
def emailContent() :
    #Isi Pesan
    ctEmail=[]
    str1=''
    for y in isiEmail[3:] :
        ctEmail.append(y)
    #return ctEmail  
    return (str1.join(ctEmail)) 

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
port = 465 #untuk standar SSL port
smtp_server="smtp.gmail.com" #SMTP Server Gmail
emailPengirim="fakhririzalsantosa@gmail.com" #email pengirim
emailPenerima= penerima #multiple receiver dengan list

psnEmail = MIMEMultipart()
psnEmail["Subject"] = emailSbj() #calling function
psnEmail["From"] = emailPengirim
psnEmail["To"] = ", ".join(emailPenerima)
text = emailContent() #calling function
psnEmail.attach(MIMEText(text, 'plain')) #adding text to body email

#Attachment
pathLoc = r'D:\Training\basic_python\Final-Project\atc pdf file.pdf'
atchFile = MIMEBase('application', "octet-stream") 
atchFile.set_payload(open(pathLoc, "rb").read()) #rb translation non-text file
encoders.encode_base64(atchFile) #encoding ke base64 - biner menjadi teks
#Read file name & Type
paths = repr(pathLoc) #mngembalikan representasi object
postNm=paths.rfind("\\")+1
atchName=str(paths[postNm:].replace("'",""))    
atchFile.add_header('Content-Disposition', 'attachment', filename=atchName)
psnEmail.attach(atchFile)

'''[Program] Input Process'''
try :
    print('Email Pengirim : '+emailPengirim)
    password = getpass.getpass('Masukan password : ')
except Exception as error:
    print("Terjadi Error")
else :
    print("Harap tunggu, program sedang melakukan pengiriman")

'''Process Pengiriman Email'''
context = ssl.create_default_context() #membuat ssl context yang paling highly recommended
with smtplib.SMTP_SSL(smtp_server, port, context=context) as emailServer :
    try :
        #Proses login
        emailServer.login(emailPengirim, password)
        #Pengiriman email disini
        emailServer.sendmail(emailPengirim, emailPenerima,psnEmail.as_string()) 
        emailServer.quit() #koneksi akan secara otomatis close saat program selesai dieksesusi
    except Exception as error:
        print("Terjadi kesalahan :(")
    else :
        os.system('cls')
        totalRecpt = len(rcpEmail)
        print("E-Mail Telah Terkirim ke-", totalRecpt, "penerima!")
        print("-------------------------------------")
        i=0
        while i < totalRecpt :
            print(rcpEmail[i].strip())
            i +=1