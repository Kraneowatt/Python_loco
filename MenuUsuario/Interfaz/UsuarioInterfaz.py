import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date, timedelta
from functools import partial
class UsuarioInterfaz:
    """
    Clase para manejar la interfaz gráfica del usuario registrado.
    """
    def __init__(self, usuario_logica):
        self.usuario_logica = usuario_logica

    def mostrar_dashboard(self, user_id):
        """
        Muestra el panel principal del usuario.
        """

        usuario_window = tk.Toplevel()
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
        date_label = tk.Label(main_frame, 
                         text="Hoy es: " + datetime.now().strftime("%d/%m/%Y"),
                         font=("Arial", 10), 
                         bg="#f2f2f2")
        date_label.pack(anchor='w')

        # Botones para las funciones del usuario

        btn_prediccion = tk.Button(main_frame, text="Ver Predicción", font=("Arial", 12), bg="#4CAF50", fg="white",
                                   command=self.usuario_logica.mostrar_prediccion)  # Ejemplo de entrada
        btn_prediccion.pack(pady=10)

        btn_trivia = tk.Button(main_frame, text="Trivia", font=("Arial", 12), bg="#4CAF50", fg="white",
                                  command=self.usuario_logica.trivia)
        btn_trivia.pack(pady=10)

        btn_notifiacion = tk.Button(main_frame, text="notificaciones", font=("Arial", 12), bg="#2196F3", fg="white",
                                          command=partial(self.usuario_logica.open_notifications,user_id))
        btn_notifiacion.pack(pady=10)

        btn_ajustes = tk.Button(main_frame, text="ajustes ", font=("Arial", 12), bg="#2196F3", fg="white",command=partial(self.usuario_logica.open_settings,user_id))
        btn_ajustes.pack(pady=10)

        btn_realizar_encuesta = tk.Button(main_frame, text="realizar encuesta diaria ", font=("Arial", 12), bg="#2196F3", fg="white",command=partial(self.usuario_logica.realizar_encuesta,user_id))
        btn_realizar_encuesta.pack(pady=10)

        btn_logout = tk.Button(main_frame, text="Cerrar Sesión", font=("Arial", 12), bg="#f44336", fg="white",
                               command=partial(self.usuario_logica.cerrar_sesion,usuario_window))
        btn_logout.pack(pady=10)
