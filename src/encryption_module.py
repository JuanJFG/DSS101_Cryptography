import random
import string
from sympy import primerange

def generate_large_prime():
    """Genera un número primo grande dentro de un rango especificado para la generación de claves."""
    primes = list(primerange(1000000, 2000000))
    return random.choice(primes)

def generate_key(seed, prime, size=64):
    """
    Genera una clave criptográfica de 64 bits utilizando una semilla y un número primo.
    Args:
    Semilla: La semilla utilizada para el generador de números aleatorios.
    primo: Un número primo grande para el cálculo de la clave.
    tamaño: El tamaño en bits de la clave, por defecto es 64 bits.
    Devuelve:
    Un entero que representa la clave criptográfica.
    """
    random.seed(seed)
    key = random.getrandbits(size)
    key = (key * prime) % (1 << size)  # Apply modular arithmetic to keep key within range
    return key

def encrypt_message(message, key):
    """
    Cifra un mensaje utilizando una simple operación XOR con fines de demostración.
    Args:
    Mensaje: El mensaje a cifrar (cadena).
    clave: La clave criptográfica (entero).
    Devuelve:
    El mensaje cifrado como una cadena que contiene todos los caracteres ASCII imprimibles.
    """
    key %= 256  # Ensure key is within range (0-255) for XOR operation
    valid_chars = string.printable
    encrypted_message = ''.join(char for char in ''.join(chr(ord(char) ^ key) for char in message) if char in valid_chars)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Descifra un mensaje mediante una simple operación XOR.
    Args:
    mensaje_encriptado: El mensaje cifrado (cadena).
    clave: La clave criptográfica utilizada para el cifrado (entero).
    Devuelve:
    El mensaje descifrado como cadena.
    """
    key %= 256  # Ensure key is within range (0-255) for XOR operation
    decrypted_message = ''.join(chr(ord(char) ^ key) for char in encrypted_message)
    return decrypted_message
