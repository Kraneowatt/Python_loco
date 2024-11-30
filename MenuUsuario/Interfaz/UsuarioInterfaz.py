import tkinter as tk
from tkinter import messagebox

class UsuarioInterfaz:
    """
    Clase para manejar la interfaz gráfica del usuario registrado.
    """
    def __init__(self, root, usuario_logica):
        self.root = root
        self.usuario_logica = usuario_logica

    def mostrar_dashboard(self, user_id):
        """
        Muestra el panel principal del usuario.
        """
        usuario_window = tk.Toplevel(self.root)
        usuario_window.title("Good Airs - Usuario")
        usuario_window.geometry("800x600")
        usuario_window.config(bg="#f2f2f2")

        main_frame = tk.Frame(usuario_window, bg="#f2f2f2")
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título y bienvenida
        current_username = self.usuario_logica.obtener_nombre_usuario(user_id)
        welcome_label = tk.Label(main_frame, 
                                 text=f"Bienvenido, {current_username}", 
                                 font=("Arial", 14, "bold"), bg="#f2f2f2")
        welcome_label.pack(pady=20)

        # Botones para las funciones del usuario
        btn_ver_datos = tk.Button(main_frame, text="Ver Datos Climáticos", font=("Arial", 12), bg="#4CAF50", fg="white",
                                  command=self.usuario_logica.ver_datos_climaticos)
        btn_ver_datos.pack(pady=10)

        btn_realizar_encuesta = tk.Button(main_frame, text="Realizar Encuesta Diaria", font=("Arial", 12), bg="#2196F3", fg="white",
                                          command=self.usuario_logica.realizar_encuesta)
        btn_realizar_encuesta.pack(pady=10)

        btn_logout = tk.Button(main_frame, text="Cerrar Sesión", font=("Arial", 12), bg="#f44336", fg="white",
                               command=usuario_window.destroy)
        btn_logout.pack(pady=10)
