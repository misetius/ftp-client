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





soketti.send(("PASV\r\n").encode("utf-8"))
data = soketti.recv(1024).decode()
data = data[26:].strip("(")
data = data[:len(data)-4]
data = data.split(",")
print(data)

porttipasv = int(data[-2]) * 256 + int(data[-1])
print(porttipasv)

soketti2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soketti2.connect((ip, porttipasv))

soketti.send(("LIST\r\n").encode("utf-8"))
print(soketti.recv(1024).decode())
print(soketti2.recv(1024))
print(soketti.recv(1024))
soketti2.close()

lahetetaanko = "k"#input("Haluatko lähettää tiedoston (k, e): ")

if lahetetaanko == "e":
    tiedostonimi = input("Syötä tiedoston nimi: ")
    soketti.send(("TYPE A\r\n").encode("utf-8"))
    print(soketti.recv(1024))
    soketti.send(("PASV\r\n").encode("utf-8"))
    data = soketti.recv(1024).decode()
    data = data[26:].strip("(")
    data = data[:len(data)-4]
    data = data.split(",")
    print(data)



    porttipasv = int(data[-2]) * 256 + int(data[-1])
    print(porttipasv)

    soketti2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soketti2.connect((ip, porttipasv))

    soketti.send((f"STOR {tiedostonimi}\r\n").encode("utf-8"))
    print(soketti.recv(1024).decode())
    tiedosto2 = open(tiedostonimi, "r").read()
    
    soketti2.send((tiedosto2+"\r\n").encode("utf-8"))
    soketti2.close()
    print(soketti.recv(1024))


ladataanko = input("Haluatko ladata tiedoston (k, e): ")
if ladataanko == "k":
    tiedostonimi = input("Syötä tiedoston nimi: ")
    binaarinavaiascii = input("Haluatko ladata tiedoston binaarina(bi) vai ASCII(as)?")
    if binaarinavaiascii == "as":

        soketti.send(("TYPE A\r\n").encode("utf-8"))
        print(soketti.recv(1024))
        soketti.send(("PASV\r\n").encode("utf-8"))
        data = soketti.recv(1024).decode()
        data = data[26:].strip("(")
        data = data[:len(data)-4]
        data = data.split(",")
        



        porttipasv = int(data[-2]) * 256 + int(data[-1])
        print(porttipasv)

        soketti2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soketti2.connect((ip, porttipasv))

        soketti.send((f"RETR {tiedostonimi}\r\n").encode("utf-8"))
        print(soketti.recv(1024).decode())
        tiedosto2 = open(tiedostonimi, "w")
    
        data = soketti2.recv(1024).decode()

        tiedosto2.write(data)

        soketti2.close()
        print(soketti.recv(1024))

if binaarinavaiascii == "bi":

        soketti.send(("TYPE I\r\n").encode("utf-8"))
        print(soketti.recv(1024))
        soketti.send(("PASV\r\n").encode("utf-8"))
        data = soketti.recv(1024).decode()
        data = data[26:].strip("(")
        data = data[:len(data)-4]
        data = data.split(",")
        



        porttipasv = int(data[-2]) * 256 + int(data[-1])
        print(porttipasv)

        soketti2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soketti2.connect((ip, porttipasv))

        soketti.send((f"RETR {tiedostonimi}\r\n").encode("utf-8"))
        print(soketti.recv(1024).decode())
        tiedosto2 = open(tiedostonimi, "w")
    
        data = soketti2.recv(1024).decode()

        tiedosto2.write(data)

        soketti2.close()
        print(soketti.recv(1024))




    
    