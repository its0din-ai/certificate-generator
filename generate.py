from pydoc import doc
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import time
import os

def banner():
    print("""====================================================
Sertif Name Generator
By ::: encrypt0r
Version 0.2-dev
====================================================""")

def requirement_check():
    banner()
    globalPath = "./"
    outputPath = "./output/"
    isDir = os.path.isdir(outputPath)

    if not isDir:
        print("Creating output DIR..")
        time.sleep(.5)
        os.mkdir(outputPath)
    else:
        print("Output DIR [OK]")
        time.sleep(.5)

    isFont = os.path.isfile(globalPath + "font.ttf")
    if not isFont:
        print("Font file not found..")
        print("Please put font.ttf in this directory")
        print("Exiting..")
        exit()
    else:
        print("Font file [OK]")
        time.sleep(.5)

    isTemplate = os.path.isfile(globalPath + "cert.png")
    if not isTemplate:
        print("Certificate template not found..")
        print("Please put cert.png in this directory")
        print("Exiting..")
        exit()
    else:
        print("Template file [OK]")
        time.sleep(.5)

    isData = os.path.isfile(globalPath + "data.csv")
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
agar font tidak terlalu kecil
.
index data ke-1 adalah header pada table CSV
perhitungan mulai data Nama index ke 2
====================================================""")
    dat = pd.read_csv('data.csv')
    for i, j in dat.iterrows():
        szz = 0
        for k in j.values:
            szz += len(k)
            info = f"ID ke-{i+2} OK"
            if szz <= 17:
                fontS = 90
                print(info)
            elif szz <= 23:
                fontS = 70
                print(info)
            elif szz <= 29:
                fontS = 60
                print(info)
            elif szz <= 35:
                fontS = 50
                print(info)
            elif szz <= 41:
                fontS = 40
                print(info)
            else:
                info = f"ID ke-{i+2} ERROR :: Name too Long"
                print(info)
                fontS = 10

            time.sleep(.5)
            font = ImageFont.truetype('font.ttf', size=fontS)
            img = Image.open('cert.png')
            tulis = ImageDraw.Draw(img)
            tulis.text(xy=(764, 434), anchor="ms", text=f"{j['name']}", fill=(0,0,0), font=font)
            img.save(f"./output/{j['name']}.png")


def main():
    if requirement_check():
        generate_starto()
        print("-------------------------------------")
        print("Done..")
        time.sleep(.5)
        print("Saved to ./output/")
        time.sleep(.2)

if __name__ == "__main__":
    main()