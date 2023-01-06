
import pickle
import random

class Tankas:

    def __init__(self):
        self.x_kryptis = 0
        self.y_kryptis = 0
        self.kryptis = 'Šiaurė'
        self.suviai = {'Šiaurė': 0, 'Pietūs': 0, 'Rytai': 0, 'Vakarai': 0}

    def pirmyn(self):
        if self.kryptis == 'Šiaurė':
            self.y_kryptis += 1
        elif self.kryptis == 'Pietūs':
            self.y_kryptis -= 1
        elif self.kryptis == 'Rytai':
            self.x_kryptis += 1
        elif self.kryptis == 'Vakarai':
            self.x_kryptis -= 1

    def atgal(self):
        if self.kryptis == 'Šiaurė':
            self.y_kryptis -= 1
        elif self.kryptis == 'Pietūs':
            self.y_kryptis += 1
        elif self.kryptis == 'Rytai':
            self.x_kryptis -= 1
        elif self.kryptis == 'Vakarai':
            self.x_kryptis += 1

    def kairen(self):
        if self.kryptis == 'Šiaurė':
            self.kryptis = 'Vakarai'
        elif self.kryptis == 'Pietūs':
            self.kryptis = 'Rytai'
        elif self.kryptis == 'Rytai':
            self.kryptis = 'Šiaurė'
        elif self.kryptis == 'Vakarai':
            self.kryptis = 'Pietūs'

    def desinen(self):
        if self.kryptis == 'Šiaurė':
            self.kryptis = 'Rytai'
        elif self.kryptis == 'Pietūs':
            self.kryptis = 'Vakarai'
        elif self.kryptis == 'Rytai':
            self.kryptis = 'Pietūs'
        elif self.kryptis == 'Vakarai':
            self.kryptis = 'Šiaurė'


    def suvis(self):
        self.suviai[self.kryptis] += 1
        suvis = random.randint(-50, 50)
        if suvis == (-2, 2):
            print("Pataikei")
        else:
            print("Nepataikei")

    def info(self):
        print(f"Koordinatės: (X - {self.x_kryptis}, Y - {self.y_kryptis})")
        print(f"Kryptis: {self.kryptis}")
        print(f"Šuvių skaičius: {self.suviai}")


    def issaugoti_duomenis(self):
        with open("info.pkl", "wb") as file:
            pickle.dump(info, file)

        with open("info.pkl", "rb") as file:
            print(pickle.load(file))

info = []
veiksmas = ""



