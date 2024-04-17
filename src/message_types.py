class Message:
    def __init__(self, data, message_type):
        self.data = data
        self.message_type = message_type

    def handle_message(self):
        """Método para manejar el mensaje, que debe ser sobrescrito por subclases."""
        raise NotImplementedError("Este método debe ser sobrescrito por subclases.")

class FirstContactMessage(Message):
    def handle_message(self):
        return f"Procesando primer contacto con datos: {self.data}"

class RegularMessage(Message):
    def handle_message(self):
        return f"Procesando mensaje regular con datos: {self.data}"

class KeyUpdateMessage(Message):
    def handle_message(self):
        return f"Procesando actualización de clave con datos: {self.data}"

class LastContactMessage(Message):
    def handle_message(self):
        return f"Procesando mensaje de finalización de sesión con datos: {self.data}"
