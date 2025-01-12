nameIn = input('Enter name: ')
if len(nameIn) < 2 or len(nameIn) > 15:
    print('Invalid name')
passwordIn = input('Enter password: ')

missingChars = []
pswd = []
if len(passwordIn) >= 8 or len(passwordIn) <= 12:
    for i in range(len(passwordIn)):
        pswd.append(passwordIn[i])
    for i in range(len(pswd)):
        if pswd[i].isalpha() == False:
            missingChars[0] += 1
        if pswd[i].isdigit() == False:
            missingChars[1] += 1
        if pswd[i].isupper() == False:
            missingChars[2] += 1
        if pswd[i].islower() == False:
            missingChars[3] += 1

