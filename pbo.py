class Segitiga:

    def __init__(self, alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi


    def get_luas(self):
        return 0.5 * self.alas * self.tinggi
Segitiga1 = Segitiga(5, 10)
Segitiga2 = Segitiga(10, 15)
Segitiga3 = Segitiga(15, 20)
print('luas segitiga1:',Segitiga1.get_luas())
print('luas segitiga2:',Segitiga2.get_luas())
print('luas segitiga3:',Segitiga3.get_luas())