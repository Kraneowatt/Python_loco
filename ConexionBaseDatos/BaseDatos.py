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
            conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=DESKTOP-ERHEOKF\SQLEXPRESS;'
                'DATABASE=Hola;'
                'Trusted_Connection=yes;'
            )
            return conexion
        except Exception as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")
            return None

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        if self.conexion:
            self.conexion.close()
