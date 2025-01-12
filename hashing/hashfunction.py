def asciiAdd(word, table_size):
    """Compute a simple hash of a given word, for a table of given size."""
    return sum(ord(char) for char in word) % table_size

def checkHashTable(hash_val, word, hash_array):
    """Insert a word into the hash table, using linear probing for collision resolution."""
    if hash_array[hash_val] == '':
        hash_array[hash_val] = word
    else:
        new_hash_val = (hash_val + 1) % len(hash_array)
        checkHashTable(new_hash_val, word, hash_array)

table_size = 20
hash_array = [''] * table_size

inp_str = input("Enter a string: ")
for word in inp_str.split():
    hashNum = asciiAdd(word, table_size)
    checkHashTable(hashNum, word, hash_array)

print(hash_array)