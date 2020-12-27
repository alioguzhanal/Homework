
ad = "Mustafa"
soyad = "Kemal"

ogrAd = input("Adınızı giriniz: ")
ogrSoyad = input ("Soyadınızı giriniz:")

print(f"Öğrenci adı:{ogrAd}")
print(f"Öğrenci soyadı:{ogrSoyad}")

k = 1
while k<=3:
    if(ogrAd == ad and ogrSoyad ==soyad):
        print("Adınızı ve soyadınızı doğru girdiniz")
        break


    elif (ogrAd == ad and ogrSoyad != soyad):
        print("Soyadınızı yanlış girdiniz")
        break


    elif (ogrAd != ad and ogrSoyad == soyad):
        print("Adınızı yanlış girdiniz")
        break


    else:
        print("Adınızı ve soyadınızı yanlış girdiniz")
        break
k = k +1

print("Derslerinizi giriniz")
ders1 =input("Birinci dersiniz: ")
ders2 =input("İkinci dersiniz: ")
ders3 =input("Üçüncü dersiniz: ")
ders4 =input("Dördüncü dersiniz: ")
ders5 =input("Beşinci dersiniz: ")

list = [ders1,ders2,ders3,ders4,ders5]

print("En az 3 en fazla 5 ders alabilirsiniz")
i = input("Almak istediğiniz ders sayısı kaç: ")

if (3 <= i <= 5):
      print("Sınav olacağınız ders :" + list[(i+17)%3])
elif (i>5):
      print("5'ten fazla ders alamazsınız")
else:
      print("3'ten az ders alamazsınız")


notlar = {"Vize" : 30, "Final": 50, "Proje": 60}

gno = int("Vize")*0,3 + int("Final")*0,5 + int("Proje")*0,2

if (100 >= gno >90):
    print("AA aldınız")
elif (gno >= 70 ):
    print("BB aldınız")
elif (gno >= 50):
    print("CC aldınız")
elif (gno >= 30):
    print("DD aldınız")
else:
    print("FF aldınız")











