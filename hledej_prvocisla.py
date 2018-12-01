# Paralelni hledani prvocisel

from prvocislo_test import je_prvocislo
from threading import Thread

class HledacPrvocisel(Thread):
    def __init__(self, d, h):
        super().__init__()
        self.dolni_mez = d
        self.horni_mez = h

    def run(self):
        for i in range(self.dolni_mez, self.horni_mez):
            if je_prvocislo(i):
                print(self.name, i)

# end class

# Vytvorime vlakna
vlakno1 = HledacPrvocisel(1, 50000)
vlakno2 = HledacPrvocisel(50000, 100000)

# Spustime je
print("Paralelni beh startuje...")
vlakno1.start()
vlakno2.start()

# Cekame na jejich dokonceni
vlakno1.join()
vlakno2.join()
print("Paralelni beh dokoncen")

