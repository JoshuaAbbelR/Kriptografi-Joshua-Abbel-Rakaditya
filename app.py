from flask import Flask, render_template, request
from ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from ciphers.playfair import playfair_encrypt, playfair_decrypt
from ciphers.hill import hill_encrypt, hill_decrypt

app = Flask(__name__)

def remove_spaces(text):
    return text.replace(' ', '').replace('\n', '').replace('\r', '')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    
    if request.method == 'POST':
        message = request.form['message'] if 'message' in request.form else ''
        key = request.form['key']
        
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            message = file.read().decode('utf-8')

        message = remove_spaces(message)
        key = remove_spaces(key)

        if len(key) < 12:
            result = "Key must be at least 12 characters long."
        else:
            cipher = request.form['cipher']
            action = request.form['action']
            
            if cipher == 'vigenere':
                if action == 'Encrypt':
                    result = vigenere_encrypt(message, key)
                else:
                    result = vigenere_decrypt(message, key)
            elif cipher == 'playfair':
                if action == 'Encrypt':
                    result = playfair_encrypt(message, key)
                else:
                    result = playfair_decrypt(message, key)
            elif cipher == 'hill':
                if action == 'Encrypt':
                    result = hill_encrypt(message, key)
                else:
                    result = hill_decrypt(message, key)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
