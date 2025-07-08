#soru-3
# girilen sayının 0-100 arasında olup olmadığını kontrol et

try:
    sayi=int(input("sayı giriniz: "))
    result=(sayi>0) and (sayi<=100)
    if result:
        print(f"sayı 0-100 arasındadır")
    else:
        print("sayı 0-100 arasında değildir")
        
except:
   print(f"!!!! Bir sayı girmelisiniz !!!")

