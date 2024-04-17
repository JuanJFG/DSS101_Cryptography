from src.encryption_module import generate_large_prime, generate_key, encrypt_message, decrypt_message
from src.message_types import FirstContactMessage, RegularMessage, KeyUpdateMessage, LastContactMessage

def get_user_input():
    """Gets user input for message, message type, and filename."""
    user_message = input("Introduce tu mensaje:\n")
    message_type = input("Introduce el tipo de mensaje (FCM, RM, KUM, LCM):\n")
    filename = input("Introduce el nombre del archivo para guardar el mensaje cifrado:\n")
    return user_message, message_type, filename

def main():
    """Main function to handle user interaction."""
    print("Elige una opción:")
    print("1. Cifrar y guardar un nuevo mensaje")
    print("2. Descifrar un mensaje de un archivo")
    choice = input("Introduce la elección (1 o 2): ")

    if choice == '1':
        prime = generate_large_prime()
        seed = 42  # Semilla fija de ejemplo para demostración
        key = generate_key(seed, prime)

        user_message, message_type, filename = get_user_input()
        
        if message_type == "FCM":
            msg = FirstContactMessage(user_message, message_type)
        elif message_type == "RM":
            msg = RegularMessage(user_message, message_type)
        elif message_type == "KUM":
            msg = KeyUpdateMessage(user_message, message_type)
        elif message_type == "LCM":
            msg = LastContactMessage(user_message, message_type)
        else:
            print("Tipo de mensaje inválido")
            return

        action_result = msg.handle_message()
        print(action_result)

        encrypted_message = encrypt_message(msg.data, key)
        print(f"Dato cifrado: {encrypted_message}")

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Mensaje cifrado: {encrypted_message}\n")
            file.write(f"Clave: {key}\n")

    elif choice == '2':
        filename = input("Introduce el nombre del archivo para descifrar: ")
        with open(filename, "r") as file:
            lines = file.readlines()
            received_encrypted_message = lines[0].strip().split(": ")[1]
            received_key = int(lines[1].strip().split(": ")[1])

        decrypted_message = decrypt_message(received_encrypted_message, received_key)
        print(f"Mensaje descifrado: {decrypted_message}")

if __name__ == "__main__":
    main()
