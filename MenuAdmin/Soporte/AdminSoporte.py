from tkinter import messagebox
import pandas as pd


class AdminSoporte:
    def __init__(self, conexion_bd):
        self.conexion_bd = conexion_bd
    @staticmethod
    def validar_dato_existente(df, column_name, value):
        """
        Verifica si un valor ya existe en el dataset en la columna especificada.
        """
        if value in df[column_name].values:
            messagebox.showerror("Error", f"El valor '{value}' ya existe en la columna {column_name}.")
            return True
        return False

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

    @staticmethod
    def cargar_dataset(file_path):
        """
        Carga el dataset desde un archivo CSV.
        """
        try:
            df = pd.read_csv(file_path, sep=',', encoding='utf-8')
            return df
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
            return None

    @staticmethod
    def guardar_dataset(file_path, df):
        """
        Guarda el dataset a un archivo CSV.
        """
        try:
            df.to_csv(file_path, sep=',', index=False, encoding='utf-8')
            messagebox.showinfo("Éxito", "El dataset ha sido guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    
    def get_today_surveys(self):
        conn = self.conexion_bd.conectar()
        cursor = conn.cursor()
        query = """
        SELECT u.idUsuario, u.nombre, u.username, e.fecha, e.eficacia, e.precision, e.interaccion, e.comentario
        FROM EncuestaDiaria e
        JOIN Usuario u ON e.idUsuario = u.idUsuario
        WHERE e.fecha = CAST(GETDATE() AS DATE)
        ORDER BY e.fecha DESC
        """
        cursor.execute(query)
        surveys = cursor.fetchall()
        conn.close()
        return surveys
