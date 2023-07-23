import os

def hitung_kecepatan():
    print("hitung kecepatan ready 🥱!")
    jarak = float(input("masukan jarak: "))
    waktu = float(input("masukan waktu: "))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan)


def luas_segitiga():
    print("hitung segitiga 😫!")
    alas = float(input("masukan alas: "))
    tinggi = float(input("masukan tinggi: "))
    luas = 0.5 * (alas * tinggi)
    print("luas segitiga adalah: ", luas, "\n")


def luas_balok():
    print("hitung luas Balok 😫!")
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    tinggi = float(input("masukan tinggi: "))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok adalah: ", luas, "\n")


def luas_bola():
    print("hitung luas bola 😫!")
    r = float(input("masukan jari-jari: "))         
    luas = 4 * 3.14 * (r**2)
    print("luas bola adalah: ", luas, "\n")

while True:
    userInput = int(input(
        "pilih rumus yang akan di pakai: \n\n1.hitung kecepatan\n2.luas segita\n3.luas_ balok\n4.luas_bola\n\n0.keluar program\n\npilih nomor berapa: "))
    os.system('clear')
    if(userInput == 1):
        hitung_kecepatan()
    elif(userInput == 2):
        luas_segitiga()
    elif(userInput == 3):
        luas_balok()
    elif(userInput == 4):
        luas_bola()
    else:
        break

hitung_kecepatan()