def find_word_positions(sentence, word):
    lower_sentence = sentence.lower().split()
    lower_word = word.lower()
    positions = []
    for i, w in enumerate(lower_sentence):
        if w == lower_word:
            positions.append(i + 1)  # Add 1 to convert to 1-based indexing
    return positions


# Example usage
sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
word = "ask"
positions = find_word_positions(sentence, word)
print(f"Word '{word}' found at positions: {positions}")
