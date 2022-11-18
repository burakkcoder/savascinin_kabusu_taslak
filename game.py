import random
import time


class Karakter:
    def __init__(self, karakter, can, silah, silah_gucu, kıyafet, seviye):
        self.karakter = karakter
        self.can = can
        self.silah = silah
        self.silah_gucu = silah_gucu
        self.kıyafet = kıyafet
        self.seviye = seviye

    def __repr__(self):
        return f"Karakter Özellikleri:\nTür : {self.karakter}\nSeviye : {self.seviye}\nCan : {self.can}\nSilah : {self.silah}\nSilah Gücü : {self.silah_gucu}\nKıyafet : {self.kıyafet}"

    def ilerle(self):
        ilerleme = [
            ".     ",
            " .    ",
            "  .   ",
            "   .  ",
            "    . ",
            "     .",
            "    . ",
            "   .  ",
            "  .   ",
            " .    ",
        ]
        i = 0
        while i < 5:
            print(ilerleme[i % len(ilerleme)], end="\r")
            time.sleep(0.5)
            i += 1

    def saldir(self, yaratik):
        oldurme_olasiligi = random.randint(0, 100)
        if yaratik - self.can > 0:
            if self.silah_gucu > 32:
                if oldurme_olasiligi < 50:
                    self.seviye += 2
                    self.can += 15
                    return True
                else:
                    self.can -= 15
                    return False
            elif self.silah_gucu > 21:
                if oldurme_olasiligi < 30:
                    self.seviye += 3
                    self.can += 30
                    return True
                else:
                    self.can -= 30
                return False
            elif self.silah_gucu > 10:
                if oldurme_olasiligi < 15:
                    self.seviye += 4
                    self.can += 45
                    return True
                else:
                    self.can -= 45
                    return False
        else:
            self.seviye += 1
            self.can += 10
            return True

    def silah_degistir(self, karakter):
        kiliclar = {"Basit Kılıç": 11,
                    "Harika Kılıç": 22, "Efsanevi Kılıç": 33}
        oklar = {"Basit Ok": 11, "Harika Ok": 22, "Efsanevi Ok": 33}
        asalar = {"Basit Asa": 11, "Harika Asa": 22, "Efsanevi Asa": 33}
        if karakter == "Savaşçı":
            silah = random.choice(list(kiliclar.items()))
            self.silah = silah[0]
            self.silah_gucu = silah[1]
        elif karakter == "Okçu":
            silah = random.choice(list(oklar.items()))
            self.silah = silah[0]
            self.silah_gucu = silah[1]
        else:
            silah = random.choice(list(asalar.items()))
            self.silah = silah[0]
            self.silah_gucu = silah[1]


print("""
********************************************************************************
Savaşçının Kabusu'na Hoş Geldin!
Yaşadığın evrendeki yeşil merada türlü yaratıklarla karşılaşacaksın.
Fakat süren kısıtlı, eğer bu meradan 2 dakika içinde sağ çıkamazsan oyun kapanır.
Seviye 10'a geldiğinde oyunu başarıyla tamamlamış olursun.
Oyunda 3 farklı silah türü olduğunu unutma, Basit, Harika ve Efsanevi.
Silahının gücü, senden güçlü yaratıkları öldürmende etkili olacaktır.
Senden güçlü yaratıkları öldürebilirsen, daha fazla can ve seviye alacaksın.
Bol Şans!
********************************************************************************
""")

yaratiklar = {"Mangyang": 70, "Büyük Gözlü Hayalet": 80, "Gelincik": 90, "Su Hayaleti": 100, "Mezar Taşı Hayaleti": 110,
              "Kırık Taş Hayaleti": 120, "Yeoha": 130, "Okçu Haydut": 140, "Kaplan": 150, "Haydut": 160, "Beyaz Kaplan": 170}

karakter_sec = input("Karakter Seçin : Savaşçı, Okçu, Büyücü\n").title()
if karakter_sec == "Savaşçı":
    karakter = Karakter("Savaşçı", 110, "Basit Kılıç", 11, "Zırh", 1)
    print(karakter)
elif karakter_sec == "Okçu":
    karakter = Karakter("Okçu", 110, "Basit Ok", 11, "Koruyucu", 1)
    print(karakter)
elif karakter_sec == "Büyücü":
    karakter = Karakter("Büyücü", 110, "Basit Asa", 11, "Cüppe", 1)
    print(karakter)
else:
    print("Lütfen karakter türünü doğru yazın!")

sure = 120
baslangic_zamani = time.time()
while time.time() < baslangic_zamani + sure:
    if karakter.seviye >= 10:
        print("Tebrikler Hayatta Kaldın!!!")
        break
    if karakter.can <= 0:
        print("Öldün - Oyun Bitti")
        break
    print("İlerliyorsun...")
    karakter.ilerle()
    yaratik, can = random.choice(list(yaratiklar.items()))
    secim = input(
        f"Karşına {yaratik}({can}) çıktı. Saldırmak ister misin? 'Evet' - 'Hayır'\n").title()
    if secim == "Evet":
        if karakter.saldir(can):
            print(f"{yaratik} öldürüldü.")
            print(
                f"Canın : {karakter.can}\nSeviyen : {karakter.seviye}\nSilah ve Gücü : {karakter.silah}-{karakter.silah_gucu}")
            sandik = input(
                "Kilitli sandık buldun. Açarsan içerisindeki silahı almak zorundasın. Kullanımda olandan düşük veya yüksek olabilir. 'Aç' - 'Açma'\n").title()
            if sandik == "Aç":
                karakter.silah_degistir(karakter.karakter)
                print(
                    f"Silah Değişti! : {karakter.silah} - Gücü : {karakter.silah_gucu}")
        else:
            print(f"{yaratik} seni çok zorladı, can kaybettin.")
            print(f"Canın : {karakter.can}\nSeviyen : {karakter.seviye}\nSilah ve Gücü : {karakter.silah}-{karakter.silah_gucu}")
    else:
        print(f"Canın : {karakter.can}\nSeviyen : {karakter.seviye}\nSilah ve Gücü : {karakter.silah}-{karakter.silah_gucu}")
        continue
