from tkinter import messagebox

class UsuarioSoporte:
    """
    Clase de soporte para tareas auxiliares del usuario.
    """
    def __init__(self, root):
        self.root = root
        
    @staticmethod
    def validar_encuesta(eficacia, precision, interaccion):
        """
        Valida si los valores de la encuesta son correctos.
        """
        if not all(1 <= i <= 5 for i in [eficacia, precision, interaccion]):
            messagebox.showerror("Error", "Los valores deben estar entre 1 y 5.")
            return False
        return True

    @staticmethod
    def mostrar_error(message):
        """
        Muestra un mensaje de error.
        """
        messagebox.showerror("Error", message)

    @staticmethod
    def mostrar_exito(message):
        """
        Muestra un mensaje de éxito.
        """
        messagebox.showinfo("Éxito", message)
