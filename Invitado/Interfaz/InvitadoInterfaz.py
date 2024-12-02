import tkinter as tk
from tkinter import messagebox

class InvitadoInterfaz:
    """
    Clase para manejar la interfaz gráfica para los invitados.
    """
    def __init__(self, root, invitado_logica):
        self.root = root
        self.invitado_logica = invitado_logica

    def mostrar_prediccion(self, datos_entrada):
        """
        Muestra la predicción del clima basada en los datos de entrada.
        """
        resultado = self.invitado_logica.obtener_prediccion_invitado()
    
        messagebox.showinfo("Predicción", resultado)

    def mostrar_resultado(self, resultado):
        """
        Muestra el resultado de la predicción.
        """
        messagebox.showinfo("Resultado de la Predicción", f"El clima será: {resultado}")

    def mostrar_error(self, mensaje):
        """
        Muestra un mensaje de error.
        """
        messagebox.showerror("Error", mensaje)

    def mostrar_ventana(self):
        """
        Muestra la ventana principal de invitado.
        """
        invitado_window = tk.Toplevel(self.root)
        invitado_window.title("Good Airs - Invitado")
        invitado_window.geometry("600x400")
        invitado_window.config(bg="#f2f2f2")

        main_frame = tk.Frame(invitado_window, bg="#f2f2f2")
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        label = tk.Label(main_frame, text="Bienvenido como Invitado", font=("Arial", 14, "bold"), bg="#f2f2f2")
        label.pack(pady=20)
        tk.Label(main_frame, text="Importante: Tienes acceso limitado al sistema general.", font=("Arial", 12), bg="#f2f2f2").pack(pady=10)
        tk.Label(main_frame, text="Para mas funcionalidades, registrate! Prueba predecir.", font=("Arial", 12), bg="#f2f2f2").pack(pady=10)

        btn_prediccion = tk.Button(main_frame, text="Ver Predicción", font=("Arial", 12), bg="#4CAF50", fg="white",
                                   command=lambda: self.mostrar_prediccion([25, 80, 1012, 15]))  # Ejemplo de entrada
        btn_prediccion.pack(pady=10)

        btn_salir = tk.Button(main_frame, text="Salir", font=("Arial", 12), bg="#f44336", fg="white", command=invitado_window.destroy)
        btn_salir.pack(pady=10)
