from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import time
import os

# GLOBAL VARIABLE
baseDir = "./"
outputDir = baseDir + "output/"
nameFont = baseDir + "font.ttf"
certIdFont = baseDir + "font-medium.ttf"
certTemplate = baseDir + "cert.png"
dataCSV = baseDir + "data.csv"

def banner():
    print("""====================================================
Sertif Name Generator
By ::: encrypt0r
Version 0.3-dev
====================================================""")

def requirement_check():
    isDir = os.path.isdir(outputDir)

    if not isDir:
        print("Creating output DIR..")
        time.sleep(.5)
        os.mkdir(outputDir)
    else:
        print("Output DIR [OK]")
        time.sleep(.5)

    isFont = os.path.isfile(nameFont)
    if not isFont:
        print("Font file not found..")
        print("Please put font.ttf in this directory")
        print("Exiting..")
        exit()
    else:
        print("Font file [OK]")
        time.sleep(.5)

    isTemplate = os.path.isfile(certTemplate)
    if not isTemplate:
        print("Certificate template not found..")
        print("Please put cert.png in this directory")
        print("Exiting..")
        exit()
    else:
        print("Template file [OK]")
        time.sleep(.5)

    isData = os.path.isfile(dataCSV)
    if not isData:
        print("CSV file not found..")
        print("Please put data.csv in this directory")
        print("Exiting..")
        exit()
    else:
        print("CSV file [OK]")
        time.sleep(.5)

    if isFont and isTemplate and isData:
        print("All requirements met..")
        time.sleep(.5)
        return True

def generate_starto():
    print("""====================================================
Generating...
----------------------------------------------------
Maks panjang nama adalah 40 Karakter,
agar font tidak menjadi terlalu kecil
====================================================""")
    speed = float(input("How Fast? lower is faster: "))
    dat = pd.read_csv(dataCSV)
    for i, j in dat.iterrows():
        f = open(f"{outputDir}log.txt", "a")
        id = j[0]
        nama = j[1]
        info = f"[+] ID ke-{id} OK"
        if len(nama) <= 17:
            fontS = 90
            f.write(info + "\n")
            print(info)
        elif len(nama) <= 23:
            fontS = 70
            f.write(info + "\n")
            print(info)
        elif len(nama) <= 29:
            fontS = 60
            f.write(info + "\n")
            print(info)
        elif len(nama) <= 35:
            fontS = 50
            f.write(info + "\n")
            print(info)
        elif len(nama) <= 41:
            fontS = 40
            f.write(info + "\n")
            print(info)
        else:
            info = f"[!] ID ke-{id} ERROR :: Name too Long"
            f.write(info + "\n")
            print(info)
            fontS = 10

        font = ImageFont.truetype(nameFont, size=fontS)
        img = Image.open(certTemplate)
        tulis = ImageDraw.Draw(img)
        tulis.text(xy=(764, 438), anchor="ms", text=f"{j['name']}", fill=(0,0,0), font=font)
        # Cert Number
        fontMedium = ImageFont.truetype(certIdFont, size=30)
        tulis.text(xy=(180, 180), anchor="ls", text=f"{j['cert_id']}", fill=(0,0,0), font=fontMedium)
        time.sleep(speed)
        f.close()
        img.save(f"{outputDir}{j['name']}.png")

def main():
    if requirement_check():
        generate_starto()
        print("-------------------------------------")
        print("Done..")
        time.sleep(.5)
        print(f"Saved to {outputDir}")
        time.sleep(.2)

if __name__ == "__main__":
    banner()

    # File STDIN
    asks = input("Do you want to change default File? [Y/n] ")
    if asks == "Y" or asks == "y":
        outputDir = baseDir + str(input("Output DIR: ")) + "/"
        nameFont = baseDir + str(input("Font File (.ttf): "))
        certIdFont = baseDir + str(input("Certificate ID Font (.ttf): "))
        certTemplate = baseDir + str(input("Certificate Template (.png): "))
        dataCSV = baseDir + str(input("Data File (.csv): "))
    elif asks == "n" or asks == "N":
        pass
    else:
        print("Invalid input..")
        exit()


    main()