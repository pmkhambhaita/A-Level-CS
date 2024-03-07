import re


def word_positions(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    word_list = []
    word_dict = {}
    position = 1

    for word in words:
        if word not in word_dict:
            word_dict[word] = position
            word_list.append(word)
            position += 1

    positions = [word_dict[word] for word in words]

    return word_list, positions


def save_to_file(word_list, positions, filename):
    with open(filename, 'w') as f:
        f.write(' '.join(word_list))
        f.write('\n')
        f.write(' '.join(map(str, positions)))


def decompress_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        word_list = lines[0].split()
        positions = list(map(int, lines[1].split()))

    sentence = ' '.join([word_list[pos - 1] for pos in positions])
    return sentence


sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU, ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
word_list, positions = word_positions(sentence)
save_to_file(word_list, positions, 'output.txt')

decompressed_sentence = decompress_file('output.txt')
print(decompressed_sentence)
