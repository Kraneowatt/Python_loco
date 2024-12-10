import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, messagebox, simpledialog
from functools import partial
class AdminInterfaz:
    """
    Clase para manejar la interfaz gráfica del administrador.
    """
    def __init__(self, root, admin_logica):
        self.root = root
        self.admin_logica = admin_logica
    

    def mostrar_dashboard(self, user_id):
        """
        Crea y muestra el panel principal del administrador.
        """
        admin_window = tk.Toplevel()
        admin_window.title("Good Airs - Admin Dashboard")
        admin_window.geometry("800x600")
        admin_window.config(bg="#e6e6e6")

        main_frame = tk.Frame(admin_window, bg="#f2f2f2")
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título
        title_label = tk.Label(main_frame, text="Administrador - Panel de Control", 
                               font=("Arial", 20, "bold"), bg="#f2f2f2")
        title_label.pack(pady=10)

        # Bienvenida y fecha
        current_username = self.admin_logica.obtener_nombre_usuario(user_id)
        welcome_label = tk.Label(main_frame, 
                                 text=f"Bienvenido a Good Airs, {current_username}", 
                                 font=("Arial", 12, "bold"), bg="#f2f2f2")
        welcome_label.pack(anchor='w', pady=5)

        date_label = tk.Label(main_frame, 
                              text="Hoy es: " + self.admin_logica.obtener_fecha_actual(), 
                              font=("Arial", 10), bg="#f2f2f2")
        date_label.pack(anchor='w', pady=5)

        # Botones
        btn_gestion = tk.Button(main_frame, text="Gestionar Dataset", 
                                font=("Arial", 12), bg="#4CAF50", fg="white",
                                command=partial(self.admin_logica.abrir_gestion_dataset,self.root))
        btn_gestion.pack(pady=10)

        btn_notificaciones = tk.Button(main_frame, text="Notificaciones", 
                                       font=("Arial", 12), bg="#2196F3", fg="white",
                                       command=partial(self.admin_logica.abrir_notificaciones,self.root))
        btn_notificaciones.pack(pady=10)

        btn_logout = tk.Button(main_frame, text="Cerrar Sesión", 
                               font=("Arial", 12), bg="#f44336", fg="white",
                               command=admin_window.destroy)
        btn_logout.pack(pady=10)

        # Información adicional
        version_label = tk.Label(main_frame, text="Versión 1.2", 
                                 font=("Arial", 10), bg="#f2f2f2")
        version_label.pack(side='bottom', pady=10)


            
