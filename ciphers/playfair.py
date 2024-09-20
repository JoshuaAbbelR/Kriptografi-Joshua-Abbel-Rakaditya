def remove_spaces(text):
    return text.replace(' ', '').replace('\n', '').replace('\r', '')

def generate_playfair_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = remove_spaces(key.upper())
    table = []
    
    for char in key:
        if char not in table and char in alphabet:
            table.append(char)
    
    for char in alphabet:
        if char not in table:
            table.append(char)
    
    return [table[i:i+5] for i in range(0, 25, 5)]

def process_digraphs(text):
    text = remove_spaces(text.upper().replace('J', 'I'))
    digraphs = []
    
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
        else:
            b = 'X'

        if a == b:
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2


    return digraphs

def find_position(table, char):
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    table = generate_playfair_table(key)
    digraphs = process_digraphs(plaintext)
    ciphertext = ''
    
    for digraph in digraphs:
        row1, col1 = find_position(table, digraph[0])
        row2, col2 = find_position(table, digraph[1])
        
        if row1 == row2:
            ciphertext += table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
        else:
            ciphertext += table[row1][col2] + table[row2][col1]
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    table = generate_playfair_table(key)
    digraphs = process_digraphs(ciphertext)
    plaintext = ''
    
    for digraph in digraphs:
        row1, col1 = find_position(table, digraph[0])
        row2, col2 = find_position(table, digraph[1])
        
        if row1 == row2:
            plaintext += table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else:
            plaintext += table[row1][col2] + table[row2][col1]
    
    return plaintext
