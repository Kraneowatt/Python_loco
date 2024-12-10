from ConexionBaseDatos.BaseDatos import ConexionBaseDatos
from tkinter import messagebox
import bcrypt
from MenuUsuario.Interfaz.UsuarioInterfaz import UsuarioInterfaz

from MenuAdmin.Interfaz.AdminInterfaz import AdminInterfaz
from ConexionBaseDatos.BaseDatos import ConexionBaseDatos

class main_soporte:
    def __init__(self,conexion_base_datos):
        self.conexion_base_datos = conexion_base_datos

    def register(self,name,username,email,password,confirm_email,confirm_password):
        
        conn =self.conexion_base_datos.conectar()

        if email != confirm_email:
            messagebox.showerror("Error", "Los correos no coinciden.")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres.")
            return

        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Usuario WHERE username = ? OR email = ?", (username, email))
            existing_user = cursor.fetchone()
            if existing_user:
                messagebox.showerror("Error", "El usuario ya existe.")
                conn.close()
                return
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            try:
                cursor.execute("""
                    EXEC sp_CrearUsuario @p_nombre = ?, 
                                        @p_username = ?, 
                                        @p_email = ?, 
                                        @p_contraseña = ?
                """, (name, username, email, hashed_password.decode('utf-8')))
                conn.commit()
                messagebox.showinfo("Éxito", "¡Usuario registrado con éxito!")
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar el usuario: {e}")
            finally:
                conn.close()

    def login_user(self,email,password):


        conn = self.conexion_base_datos.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                # Modificada la consulta para obtener todos los datos necesarios del usuario
                cursor.execute("""
                    SELECT u.idUsuario, u.contraseña, r.nombre, r.idRol
                    FROM Usuario u
                    JOIN RolDeUsuario ru ON u.idUsuario = ru.idUsuario
                    JOIN Rol r ON ru.idRol = r.idRol
                    WHERE u.email = ? and u.password=?
                """, (email,password))
                
                user = cursor.fetchone()
                
                if user and user[1].strip() == password:
                    if user[3]==2:
                        messagebox.showinfo("Login Successful", "¡Bienvenido de nuevo!")
                        user_id = user[0]  # ID del usuario que inició sesión
                        UsuarioInterfaz.open_user_window(user_id)
                    elif user[3]==1:
                        messagebox.showinfo("Login Successful", "¡Bienvenido de nuevo!")
                        user_id = user[0]  # ID del usuario que inició sesión
                        AdminInterfaz.mostrar_dashboard(user_id)
                    else:
                        messagebox.showwarning("Login Failed", "Credenciales incorrectas.")

            except Exception as e:
                messagebox.showerror("Error", f"Error durante el login: {e}")
            finally:
                conn.close()



