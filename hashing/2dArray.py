examScores = [
    ['Max', 56, 72, 43],
    ['Tom', 66, 78, 44],
    ['Bob', 42, 65, 38]
]

print(examScores[1][0], "got scores of", examScores[1][1], examScores[1][2], examScores[1][3], "on the first exam.") 

for i in range(3):
    print('IT Scores are: ')
    print(str(examScores[i][2]))

print('The scores of the students are: ')
print('Name - Maths - IT - Biology')
for i in range(len(examScores)):
    for j in range(4):
        print(examScores[i][j] , end = ' ')
    print('\n')

username = input('Enter a username: ')
for i in range(len(examScores)):
    if username in examScores[i]:
        print('The scores of', username, 'are: ')
        for j in range(1, 4):
            print(examScores[i][j], end = ' ')
        break

for i in range(len(examScores)):
    ### add 5 to biology score
    examScores[i][3] += 5
    print(examScores[i][0], 'got', examScores[i][3], 'in Biology')