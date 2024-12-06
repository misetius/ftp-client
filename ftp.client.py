
from ftplib import FTP

# Tarvittava informaatio testausta varten. 
# Salasana ja käyttäjänimi vaihtuvat ajoittain
HOSTNAME = "ftp.dlptest.com"
USERNAME = "dlpuser"
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"

with FTP(HOSTNAME) as ftp:

    ftp.login(user=USERNAME, passwd=PASSWORD)
    print(ftp.getwelcome())

    ftp.encoding = "utf-8"
    
    print(ftp.sendcmd("EPSV"))

    ftp.retrlines('LIST')
        
    lataatiedosto = input("lataa tiedosto: ")

    if len(lataatiedosto) > 1:
        with open('testi.txt', 'wb') as file:
            ftp.retrbinary(f"RETR ", {lataatiedosto}, file.write)
    else:
        print("Suljetaan yhteys")
        ftp.quit()
