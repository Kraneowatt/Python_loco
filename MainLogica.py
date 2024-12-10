import tkinter as tk
from tkinter import messagebox
from functools import partial
class MainLogica:

    def __init__(self,conexion_bd,MainSoporte):
        self.conexion_bd=conexion_bd
        self.MainSoporte=MainSoporte

    def login_user(self):
        email = entry_email.get().strip()
        password = entry_password.get().strip()

        conn =self.conexion_bd.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.idUsuario, u.contraseña, r.nombre 
                FROM Usuario u
                JOIN RolDeUsuario ru ON u.idUsuario = ru.idUsuario
                JOIN Rol r ON ru.idRol = r.idRol
                WHERE u.email = ?
            """, (email,))
            user = cursor.fetchone()

            if user:
                user_id, stored_password, role_name = user[0], user[1].strip(), user[2]
                if role_name == 'Administrador':
                    messagebox.showinfo("Login Successful", "¡Bienvenido Administrador!")
                    open_admin_window(user_id)  # Abre la ventana de administración
                    
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    if role_name == 'Usuario':
                        messagebox.showinfo("Login Successful", "¡Bienvenido de nuevo!")
                        open_user_window(user_id)  # Abre la ventana de usuario después del login exitoso
                    else:
                        messagebox.showwarning("Login Failed", "Contraseña incorrecta.")
            else:
                messagebox.showwarning("Login Failed", "No se encontró un usuario con este correo.")

            conn.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")


    # Función para abrir la ventana de inicio de sesión
    def open_login_window(self,root):
        global login_window, entry_email, entry_password

        # Cerrar ventana principal si está abierta
        root.withdraw()

        login_window = tk.Toplevel(root)
        login_window.title("Iniciar Sesión")
        login_window.geometry("400x500")
        login_window.config(bg="#f2f2f2")

        # Etiquetas y campos de entrada
        tk.Label(login_window, text="Bienvenido a Good Airs!\nInicie sesión completando los datos", font=("Arial", 12), bg="#f2f2f2").pack(pady=10)
        
        tk.Label(login_window, text="Correo", bg="#f2f2f2").pack()
        entry_email = tk.Entry(login_window, width=30)
        entry_email.pack(pady=5)

        tk.Label(login_window, text="Contraseña", bg="#f2f2f2").pack()
        entry_password = tk.Entry(login_window, show="*", width=30)
        entry_password.pack(pady=5)

        # Botón de iniciar sesión
        btn_login = tk.Button(login_window, text="Iniciar Sesión", command=self.login_user, bg="#4CAF50", fg="white", font=("Arial", 12))
        btn_login.pack(pady=10)

        # Botón de "Olvidé la contraseña"
        btn_forgot_password = tk.Button(login_window, text="Olvidaste la contraseña?", command=lambda: messagebox.showinfo("Info", "Funcionalidad en construcción"), bg="#FFC107", fg="white", font=("Arial", 10))
        btn_forgot_password.pack()


    def open_register_window(self,root):
        print("Open Register window.")  # Mensaje de depuración para asegurarse de que esta función es llamada.
        
        # Cerrar ventana principal si está abierta
        root.withdraw()

        register_window = tk.Toplevel(root)  # Crear una nueva ventana
        register_window.title("Registrar")
        register_window.geometry("400x500")
        register_window.config(bg="#f2f2f2")

        # Etiqueta de bienvenida
        tk.Label(register_window, text="Bienvenido a Good Airs!\nLlene los datos para continuar!", font=("Arial", 14, "bold"), bg="#f2f2f2").grid(row=0, column=0, columnspan=2, pady=10)

        # Crear y ubicar las etiquetas y campos de entrada con el layout grid
        tk.Label(register_window, text="Nombre", bg="#f2f2f2").grid(row=1, column=0, padx=20, pady=5, sticky="w")
        entry_name = tk.Entry(register_window, width=30)
        entry_name.grid(row=1, column=1, padx=20, pady=5)

        tk.Label(register_window, text="Nombre de Usuario", bg="#f2f2f2").grid(row=2, column=0, padx=20, pady=5, sticky="w")
        entry_username = tk.Entry(register_window, width=30)
        entry_username.grid(row=2, column=1, padx=20, pady=5)

        tk.Label(register_window, text="Correo", bg="#f2f2f2").grid(row=3, column=0, padx=20, pady=5, sticky="w")
        entry_email = tk.Entry(register_window, width=30)
        entry_email.grid(row=3, column=1, padx=20, pady=5)

        tk.Label(register_window, text="Contraseña", bg="#f2f2f2").grid(row=4, column=0, padx=20, pady=5, sticky="w")
        entry_password = tk.Entry(register_window, width=30, show="*")
        entry_password.grid(row=4, column=1, padx=20, pady=5)

        tk.Label(register_window, text="Confirmar Contraseña", bg="#f2f2f2").grid(row=5, column=0, padx=20, pady=5, sticky="w")
        entry_confirm_password = tk.Entry(register_window, width=30, show="*")
        entry_confirm_password.grid(row=5, column=1, padx=20, pady=5)

        tk.Label(register_window, text="Confirmar Correo", bg="#f2f2f2").grid(row=6, column=0, padx=20, pady=5, sticky="w")
        entry_confirm_email = tk.Entry(register_window, width=30)
        entry_confirm_email.grid(row=6, column=1, padx=20, pady=5)

        # Botón de registro
        btn_register = tk.Button(register_window, text="Registrar", command=partial(self.register_user,entry_name, entry_username, entry_email, entry_password, entry_confirm_email, entry_confirm_password), bg="#4CAF50", fg="white", font=("Arial", 12))
        btn_register.grid(row=7, column=0, columnspan=2, pady=20)


    # Función para registrar el usuario
    def register_user(self,entry_name, entry_username, entry_email, entry_password, entry_confirm_email, entry_confirm_password):
        print("Register button clicked.")  # Mensaje de depuración para verificar si la función es llamada.
        name = entry_name.get()
        username = entry_username.get()
        email = entry_email.get()
        password = entry_password.get()
        confirm_email = entry_confirm_email.get()
        confirm_password = entry_confirm_password.get()

        self.MainSoporte.register(name,username,email,password,confirm_email,confirm_password)

    # Crear ventana de registro
    
    # Ventana para el usuario invitado
    def open_guest_window():
        guest_window = tk.Toplevel(root)
        guest_window.title("Acceso como Invitado")
        guest_window.geometry("400x300")
        guest_window.config(bg="#f2f2f2")
        tk.Label(guest_window, text="Bienvenido Invitado!", font=("Arial", 14), bg="#f2f2f2").pack(pady=20)
        tk.Label(guest_window, text="Importante: Tienes acceso limitado al sistema general.", font=("Arial", 12), bg="#f2f2f2").pack(pady=10)
        tk.Label(guest_window, text="Para mas funcionalidades, registrate! Prueba predecir.", font=("Arial", 12), bg="#f2f2f2").pack(pady=10)
        date_label = tk.Label(guest_window, 
                            text="Hoy es: " + datetime.now().strftime("%d/%m/%Y"),
                            font=("Arial", 10), 
                            bg="#f2f2f2")
        date_label.pack(anchor='w')

        prediction_btn = tk.Button(guest_window, text="Predecir", command=show_predictionguest,
                                bg="#4CAF50", fg="white", width=55)
        prediction_btn.pack(anchor='w', pady=5)
        
        

    # Crear ventana principal
