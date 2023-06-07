import time

def geri_sayim(saniye):
    while saniye >0:
        print(saniye)
        time.sleep(1)
        saniye -= 1
    print("Geri sayım tamamlandı!")

saniye = int(input("Kaç saniyeden geriye doğru saymak istersiniz? "))
geri_sayim(saniye)