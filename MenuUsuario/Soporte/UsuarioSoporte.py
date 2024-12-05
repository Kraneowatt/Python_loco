from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, date, timedelta
import tkinter as tk

class UsuarioSoporte:
    """
    Clase de soporte para tareas auxiliares del usuario.
    """
    def __init__(self, root,conexion_bd):
        self.conexion_bd = conexion_bd
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

    def mostrar_encuesta(self,notif_window,user_id):
        conn =self.conexion_bd.conectar()
        if conn is None:
            messagebox.showerror("Database Error", "No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            cursor.execute("""
                           SELECT DISTINCT CONVERT(date, fecha) 
                           FROM EncuestaDiaria 
                           WHERE idUsuario = ?
                           """, (user_id,))
            completed_dates = [row[0] for row in cursor.fetchall()]
            today = date.today()
            missed_days = []
            
            start_date = date(2024, 11, 13)
            days_diff = (today - start_date).days
            
            for day in range(days_diff + 1):
                date_to_check = start_date + timedelta(days=day)
                if date_to_check not in completed_dates:
                    missed_days.append(date_to_check)
            
            if missed_days:
                for missed_day in missed_days:
                    tk.Label(notif_window, text=f"No completaste la encuesta del día {missed_day}.", font=("Arial", 10)).pack()
            else:
                tk.Label(notif_window, text="Has completado todas las encuestas de los días anteriores.", font=("Arial", 10)).pack()
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener notificaciones: {e}")
        finally:
            cursor.close()
        conn.close()

    def verificar_encuesta(self,user_id):
        conn = self.conexion_bd.conectar()
        if conn is None:
            messagebox.showerror("Database Error", "No se pudo conectar a la base de datos.")
            return False
        
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT COUNT(*) 
                       FROM EncuestaDiaria 
                       WHERE idUsuario = ? AND CONVERT(date, fecha) = CONVERT(date, GETDATE())
                       """, (user_id,))
        encuesta_completada = cursor.fetchone()[0]
        if encuesta_completada > 0:
            messagebox.showerror("Encuesta ya realizada", "Vuelva mañana, su encuesta diaria ya la hizo.")
            cursor.close()
            conn.close()
            return False
        else:
            return True
    
    def hacer_encuesta(self,user_id,eficacia,precision,interaccion,comentario,root):
        conn = self.conexion_bd.conectar()
        cursor = conn.cursor()
        cursor.execute("""
                        EXEC sp_RegistrarEncuestaDiaria 
                        @p_idUsuario = ?, @p_eficacia = ?, @p_precision = ?, 
                        @p_interaccion = ?, @p_comentario = ?
                        """, (user_id, eficacia, precision, interaccion, comentario))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Éxito", "Encuesta registrada con éxito.")
        root.destroy()

    def obtener_info(self,user_id):
        conn = self.conexion_bd.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, username FROM Usuario WHERE idUsuario = ?", (user_id,))
            user_info = cursor.fetchone()
            current_name = user_info[0] if user_info else "Usuario"
            current_username = user_info[1] if user_info else "username"
            conn.close()
            return current_name, current_username
    

    def cambiar_nombre_usuario(self,user_id, nuevo_nombre):
        conn = self.conexion_bd.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT nombre FROM Usuario WHERE idUsuario = ?", (user_id,))
                if cursor.fetchone():
                    cursor.execute("""
                        UPDATE Usuario 
                        SET nombre = ? 
                        WHERE idUsuario = ?
                    """, (nuevo_nombre, user_id))
                    conn.commit()
                    messagebox.showinfo("Éxito", f"Nombre actualizado correctamente a: {nuevo_nombre}")
                    return True
                else:
                    messagebox.showerror("Error", "Usuario no encontrado.")
                    return False
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar el nombre: {e}")
                return False
            finally:
                conn.close()
        return False

    def cambiar_username(self,user_id, nuevo_username):
        conn = self.conexion_bd.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                # Verificar si el username ya existe
                cursor.execute("SELECT idUsuario FROM Usuario WHERE username = ?", (nuevo_username,))
                if cursor.fetchone():
                    messagebox.showerror("Error", "Este nombre de usuario ya está en uso.")
                    return False
                
                cursor.execute("""
                    UPDATE Usuario 
                    SET username = ? 
                    WHERE idUsuario = ?
                """, (nuevo_username, user_id))
                conn.commit()
                messagebox.showinfo("Éxito", "Nombre de usuario actualizado correctamente.")
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar el nombre de usuario: {e}")
                return False
            finally:
                conn.close()
        return False

    def cambiar_contraseña(self,user_id, contraseña_actual, nueva_contraseña):
        conn = self.conexion_bd.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                # Verificar contraseña actual
                cursor.execute("SELECT contraseña FROM Usuario WHERE idUsuario = ?", (user_id,))
                result = cursor.fetchone()
                if result and result[0].strip() == contraseña_actual:
                    cursor.execute("""
                        UPDATE Usuario 
                        SET contraseña = ? 
                        WHERE idUsuario = ?
                    """, (nueva_contraseña, user_id))
                    conn.commit()
                    messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
                    return True
                else:
                    messagebox.showerror("Error", "La contraseña actual es incorrecta.")
                    return False
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar la contraseña: {e}")
                return False
            finally:
                conn.close()
        return False