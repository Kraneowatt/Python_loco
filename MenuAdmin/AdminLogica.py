import pandas as pd
from tkinter import messagebox
from datetime import datetime

class AdminLogica:
    """
    Clase para manejar la lógica del administrador.
    """
    def __init__(self, conexion_base_datos):
        self.conexion_base_datos = conexion_base_datos

    def obtener_nombre_usuario(self, user_id):
        """
        Obtiene el nombre del administrador desde la base de datos.
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

    def obtener_fecha_actual(self):
        """
        Devuelve la fecha actual formateada.
        """
        return datetime.now().strftime("%d/%m/%Y")

    def abrir_gestion_dataset(self):
        """
        Abre la gestión del dataset (placeholder).
        """
        messagebox.showinfo("Gestión del Dataset", "Funcionalidad en desarrollo.")

    def abrir_notificaciones(self):
        """
        Abre la ventana de notificaciones (placeholder).
        """
        messagebox.showinfo("Notificaciones", "Funcionalidad en desarrollo.")
