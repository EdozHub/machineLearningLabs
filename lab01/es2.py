import numpy as np
import sys

def readFile():
    if len(sys.argv) < 4:
        print("Non hai inserito un numero sufficiente di argomenti")
        sys.exit(1)
    matrice = np.loadtxt(sys.argv[1])
    return matrice, sys.argv[2], sys.argv[3]


def meausureDistance(matrice, bus):
    matrice = matrice[matrice[:, 0] == int(bus)]
    matrice = matrice[:, [0, 2, 3]]
    distances = np.sqrt(np.square(matrice[:, 1])+np.square(matrice[:, 2]))
    sumDistance = np.sum(distances)
    return sumDistance

def main():
    matrice, flag, bus = readFile()
    distanza = meausureDistance(matrice, bus)
    print(f"La distanza totale percorsa dal bus {bus} è {distanza}")

main()
