from tkinter import messagebox
from datetime import datetime

class UsuarioLogica:
    """
    Clase para manejar la lógica del usuario.
    """
    def __init__(self, conexion_base_datos,root):
        self.conexion_base_datos = conexion_base_datos
        self.root=root

    def obtener_nombre_usuario(self, user_id):
        """
        Obtiene el nombre del usuario desde la base de datos.
        """
        conn = self.conexion_base_datos.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT nombre FROM Usuario WHERE idUsuario = ?", (user_id,))
                result = cursor.fetchone()
                return result[0] if result else "Desconocido"
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo obtener el nombre: {e}")
            finally:
                self.conexion_base_datos.cerrar_conexion()
        return "Desconocido"

    def ver_datos_climaticos(self):
        """
        Lógica para mostrar los datos climáticos.
        """
        # Aquí podrías cargar los datos desde la base de datos o archivo
        messagebox.showinfo("Datos Climáticos", "Aquí se mostrarían los datos climáticos.")

    def realizar_encuesta(self):
        """
        Lógica para registrar una encuesta diaria.
        """
        # Implementar la lógica para realizar una encuesta
        messagebox.showinfo("Encuesta", "La encuesta diaria ha sido registrada correctamente.")
