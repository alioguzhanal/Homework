import datetime

firstName = input("Adınızı giriniz: ")
lastName = input("Soyadınızı giriniz: ")
age = int(input("Yaşınızı giriniz: "))
dateOfBirth= input("Doğduğunuz yılı giriniz: ")

liste = [firstName, lastName, age, dateOfBirth]

print(liste)


if liste[2] <= 18 :
    print("You can not go out because it is too dangerous for u")

else:
    print("You can go out to the street")



