import numpy as np
import sys

def readFile():
    if len(sys.argv) != 2:
        print("Non hai inserito tutti i parametri")
        sys.exit(1)
    
    file_path = sys.argv[1]
    data = []
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            data.append(parts)
    
    return np.array(data)

def birthsPerCity(data):
    cities = np.unique(data[:, 2])
    u_cities, counts = np.unique(cities, return_counts=True)
    return dict(zip(u_cities, counts))

def birthsPerMonth(data):
    dates = data[:, -1]
    months = np.array([dates.split("/")[1]] for date in dates)
    u_months, counts = np.unique(months, return_counts=True)
    return dict(zip(u_months, counts))


def main():
    dati = readFile()
    res = birthsPerCity(dati)
    for city, births in res.items():
        print(f"Città: {city}, Nascite: {births}")
        print("\nNascite per mese:")

    res_month = birthsPerMonth(dati)
    for month, births in res_month.items():
        print(f"Mese: {month}, Nascite: {births}")
    

if __name__ == "__main__":
    main()