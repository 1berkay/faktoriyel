print("""
************ FAKTORİYEL BULMA PROGRAMI ************


ÇIKMAK İÇİN 'q/Q' BASINIZ.


""")

faktoriyel = 1
while True:
    sayı = input("Sayı Giriniz:")
    if sayı == "Q" or sayı == "q":
        print("Sistemden çıkılıyor..")
        break
    else:
        sayı = int(sayı)
        liste = range(2,sayı+1)
        for i in liste:
            faktoriyel *= i
        print(faktoriyel)

