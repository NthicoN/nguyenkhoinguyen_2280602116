from flask import Flask, request, jsonify
from cipher.caesar import Caesarcipher
from cipher.vigenere import Vigenerecipher
from cipher.railfencer import RailfenceCipher


app = Flask(__name__)

railfence_cipher = RailfenceCipher()
@app.route("/api/railfence/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

    @app.route("/api/railfence/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(plain_text, key)
    return jsonify({'decrypted_text': decrypted_text})

vigenere_cipher = Vigenerecipher()
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

caesar_cipher = Caesarcipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def ceasar_encruypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def ceasar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    
    
    
    
    
