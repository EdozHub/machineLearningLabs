import sys

def calculateScore(points):
    minimum = min(points)
    maximum = max(points)

    points.remove(minimum)
    points.remove(maximum)

    return sum(points)

def main():
    if len(sys.argv) < 2:
        print("Non hai inserito il nome del file")
        sys.exit(1)
    filename = sys.argv[1]
    f = open(filename, 'r')
    scores = []
    competitorScore = []
    i=0
    for line in f:
       columns = line.strip().split()
       scores = [float(score) for score in columns[3:]] 
       avgScore = calculateScore(scores)
       competitorScore.append((columns[0] + " " + columns[1], avgScore))
       i += 1
    f.close()
    competitorScoreOrdinati = sorted(competitorScore, key=lambda l: l[1], reverse=True)[:3]
    print(competitorScoreOrdinati)

