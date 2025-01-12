import pickle

def hash_username(username, table_size):
    """Compute a simple hash of a given username, for a table of given size."""
    return sum(ord(char) for char in username) % table_size

def hash_password(username, password):
    hashed_password = ""
    for letter in password:
        hashed_letter = chr((ord(letter) + ord(username[0])) % 94 + 33)
        hashed_password += hashed_letter
        username = username[1:] + hashed_letter if username[1:] else username
    return hashed_password

def insert_into_hash_table(hash_table, username, password):
    """Insert a username and password into the hash table, using linear probing for collision resolution."""
    table_size = len(hash_table)
    hash_val = hash_username(username, table_size)
    while hash_table[hash_val] is not '':
        hash_val = (hash_val + 1) % table_size
    hash_table[hash_val] = (username, hash_password(username, password))

table_size = 3
hash_table = [''] * table_size

while True:
    selection = input("Enter 'e' to insert a username and password into the hash table, or v to view the hash table: ")
    if selection == 'e':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        insert_into_hash_table(hash_table, username, password)

        print("Hash table:", hash_table)

        with open('hash_table.pkl', 'wb') as f:
            pickle.dump(hash_table, f)
            print("Hash table saved to hash_table.pkl")

    if selection == 'v':
        with open('hash_table.pkl', 'rb') as f:
            hash_table = pickle.load(f)
            print("Hash table:", hash_table)
            print("Hash table loaded from hash_table.pkl")