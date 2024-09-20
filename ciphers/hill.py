def remove_spaces(text):
    return text.replace(' ', '').upper()

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_encrypt(plaintext, key):
    plaintext = remove_spaces(plaintext)
    key = remove_spaces(key)
    
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    key_matrix = [
        [ord(key[0]) - ord('A'), ord(key[1]) - ord('A')],
        [ord(key[2]) - ord('A'), ord(key[3]) - ord('A')]
    ]

    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        vector = [ord(plaintext[i]) - ord('A'), ord(plaintext[i+1]) - ord('A')]
        
        encrypted_vector = [
            (key_matrix[0][0] * vector[0] + key_matrix[0][1] * vector[1]) % 26,
            (key_matrix[1][0] * vector[0] + key_matrix[1][1] * vector[1]) % 26
        ]
        
        ciphertext += chr(encrypted_vector[0] + ord('A'))
        ciphertext += chr(encrypted_vector[1] + ord('A'))

    return ciphertext

def hill_decrypt(ciphertext, key):
    ciphertext = remove_spaces(ciphertext)
    key = remove_spaces(key)
    
    key_matrix = [
        [ord(key[0]) - ord('A'), ord(key[1]) - ord('A')],
        [ord(key[2]) - ord('A'), ord(key[3]) - ord('A')]
    ]

    determinant = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
    determinant_inv = mod_inverse(determinant, 26)
    
    if determinant_inv is None:
        raise ValueError("Determinant is not invertible in mod 26. Choose another key.")

    adjugate_matrix = [
        [key_matrix[1][1], -key_matrix[0][1]],
        [-key_matrix[1][0], key_matrix[0][0]]
    ]

    inverse_key_matrix = [
        [(determinant_inv * adjugate_matrix[0][0]) % 26, (determinant_inv * adjugate_matrix[0][1]) % 26],
        [(determinant_inv * adjugate_matrix[1][0]) % 26, (determinant_inv * adjugate_matrix[1][1]) % 26]
    ]

    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        vector = [ord(ciphertext[i]) - ord('A'), ord(ciphertext[i+1]) - ord('A')]
        
        decrypted_vector = [
            (inverse_key_matrix[0][0] * vector[0] + inverse_key_matrix[0][1] * vector[1]) % 26,
            (inverse_key_matrix[1][0] * vector[0] + inverse_key_matrix[1][1] * vector[1]) % 26
        ]
        
        plaintext += chr(decrypted_vector[0] + ord('A'))
        plaintext += chr(decrypted_vector[1] + ord('A'))

    return plaintext
