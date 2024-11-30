import pyodbc
from tkinter import messagebox

class ConexionBaseDatos:
    """
    Clase para manejar la conexión con la base de datos.
    """
    def __init__(self, driver, server, database):
        self.driver = driver
        self.server = server
        self.database = database
        self.conexion = None

    def conectar(self):
        """
        Establece la conexión con la base de datos.
        """
        try:
            self.conexion = pyodbc.connect(
                f"DRIVER={{{self.driver}}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                "Trusted_Connection=yes;"
            )
            return self.conexion
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"Error al conectar: {e}")
            return None

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        if self.conexion:
            self.conexion.close()
