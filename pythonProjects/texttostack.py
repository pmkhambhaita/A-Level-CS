word = input("Enter a word: ")
wordLength = len(word)

stack1 = ['', '', '', '', '', '', '']

headPointer = wordLength + 1
tailPointer = 0

for i in range(wordLength):
    stack1[tailPointer] = word[headPointer]
    headPointer -= 1
    tailPointer += 1

stack1[tailPointer] = wordLength

print(stack1)