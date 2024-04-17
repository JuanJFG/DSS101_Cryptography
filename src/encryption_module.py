import random
from sympy import primerange

def generate_large_prime():
    """Generates a large prime number within a specified range for key generation."""
    primes = list(primerange(1000000, 2000000))
    return random.choice(primes)

def generate_key(seed, prime, size=64):
    """
    Generates a cryptographic key of 64 bits using a seed and a prime number.

    Args:
    seed: The seed used for the random number generator.
    prime: A large prime number for key calculation.
    size: The bit size of the key, default is 64 bits.

    Returns:
    An integer representing the cryptographic key.
    """
    random.seed(seed)
    key = random.getrandbits(size)
    key = (key * prime) % (1 << size)  # Apply modular arithmetic to keep key within range
    return key

def encrypt_message(message, key):
    """
    Encrypts a message using a simple XOR operation for demonstration purposes.

    Args:
    message: The message to encrypt (string).
    key: The cryptographic key (integer).

    Returns:
    The encrypted message as a string.
    """
    key %= 256  # Ensure key is within range (0-255) for XOR operation
    return ''.join(chr(ord(char) ^ key) for char in message)

def decrypt_message(encrypted_message, key):
    """
    Decrypts a message using a simple XOR operation.

    Args:
    encrypted_message: The encrypted message (string).
    key: The cryptographic key used for encryption (integer).

    Returns:
    The decrypted message as a string.
    """
    key %= 256  # Ensure key is within range (0-255) for XOR operation
    return ''.join(chr(ord(char) ^ key) for char in encrypted_message)
