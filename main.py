from tankas import Tankas


tankas = Tankas()

while True:
    tankas.info()
    veiksmas = int(input('Išsirinkite komanda:\n1 - pirmyn \n2 - atgal \n3 - kairėn \n4 - dešinėn \n5 - šauti \n0 - išeiti \n'))
    if veiksmas == 1:
        tankas.pirmyn()
    if veiksmas == 2:
        tankas.atgal()
    if veiksmas == 3:
        tankas.kairen()
    if veiksmas == 4:
        tankas.desinen()
    if veiksmas == 5:
        tankas.suvis()
    if veiksmas == 0:
        print("Žaidimas baigtas")
        break





