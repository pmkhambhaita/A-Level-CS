minsPlayed = [
    ['James',60, 180, 200, 60, 100],
    ['Fiona', 30, 60, 30, 10, 35],
    ['Sophie', 45, 0, 0, 15, 30],
    ['Danny', 0, 60, 20, 15, 45]
]


for i in range(len(minsPlayed)):
    total = 0
    for j in range(1, len(minsPlayed[i])):
        total += minsPlayed[i][j]
    print(f'{minsPlayed[i][0]} played for {total} minutes')

       
