import socket

# Tarvittava informaatio testausta varten. 
# Salasana ja käyttäjänimi vaihtuvat ajoittain
HOSTNAME = "ftp.dlptest.com"
USERNAME = "dlpuser"
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"
portti1 = 20
portti2 = 21

soketti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(HOSTNAME)
print(ip)

soketti.connect((ip, portti2))

kirjautuminen = "USER " + USERNAME
salasana = "PASS " + PASSWORD


print(soketti.recv(1024))
soketti.send((kirjautuminen + "\r\n").encode("utf-8"))
print(soketti.recv(1024).decode())


soketti.send((salasana + "\r\n").encode("utf-8"))
print(soketti.recv(1024).decode())


    
    