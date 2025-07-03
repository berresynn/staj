name='Berre'
surname='Şüyün'
age='20'

print('my name is '+ name + ' '+ surname +' and I am ' +  age  + ' years old.')

# my name is Berre Şüyün and I am 20 years old. çıktısına ulaşırız 

# \n  bir alt satıra inmemizi sağlar 

#index numara sıfırdan başlar
#BERRE yazılıysa bunun imdex numaraları  01234 olur 
#eğer bu sağdan başlasaydı -4-3-2-1 0 olurdu 
#lenght=uzunluk
# uzun bir kelime veya cümledeki son harfin index numarası için 
# print(greeting[lenght-1]) dememiz gerekir
#greetingin burda bir önemi yoktur cümle veya kelimeyi ne olarak tanımladıysak onu yazarız

#örnek1 
# print(greeting[3:7]) 3.indexten başla 7. indexse kadar git
# my name yazıyorsa eğer  0 1 2 3 4 5 6 olur burdaki 2 sayısı boşluktaki numara ve bunun çıktısı name olur(3:7)

#print(greeting[3:]) 3ten başla sonuna kadar 
#print(greeting[:15]) baştan başla 15e kadar 
#print(greeting[2:40:2]) 2den başla 40a kadar 2şer git yani my name is yazıyorsa 0 1 2 3 4 5 6 7 8 9.... bunun çıktısı a e i .... olur 
