class Ogrenci():
    def __init__(self, numara=0):
        self.numara = numara
ogrenciler = ["Ali", "Can", "Eminem"]
atamalar = {"canan":Ogrenci()}

print(atamalar["canan"].numara)