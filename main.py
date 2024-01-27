import random
karekter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890>{[]}!@#$%^&*()"
 
şifre_uzunluk = int(input("Şifre kaç karakterden oluşturulsun : "))
şifre_count = int(input("Şifre kaç Adet oluşturulsun : "))
for i in range(0, şifre_count):
    şifre =""
    for i in range(0 , şifre_uzunluk):
        şifre_karekter = random.choice(karekter)
        şifre =  şifre + şifre_karekter
    print("Şifreniz," , şifre)
