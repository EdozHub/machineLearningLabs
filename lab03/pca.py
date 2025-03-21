import numpy as np

def readFile(filename):
    matrix = np.loadtxt(filename, delimiter=',', usecols=range(4))
    return matrix.T

# Trasposto della matrice contenuta nel file
D = readFile('iris.csv')

# Calcolo della media
mu = D.mean(1)
mu = mu.reshape(mu.size,1)

# Calcolo della matrice centrata
DC = D - mu

# Calcolo della matrice di covarianza
C = (DC @ DC.T)/(DC.shape[1])

# Calcolo degli autovalori e autovettori (s: autovalori, U: autovettori)
s, U = np.linalg.eigh(C)


