from tkinter import messagebox

class InvitadoSoporte:
    """
    Clase de soporte para tareas auxiliares del invitado.
    """
    @staticmethod
    def validar_datos(datos_entrada):
        """
        Valida los datos de entrada proporcionados por el invitado.
        """
        if not all(isinstance(i, (int, float)) for i in datos_entrada):
            messagebox.showerror("Error", "Todos los datos deben ser numéricos.")
            return False
        if len(datos_entrada) != 4:  # Supongamos que necesitamos 4 datos: temperatura, humedad, presión, viento
            messagebox.showerror("Error", "Se requieren 4 datos de entrada.")
            return False
        return True
