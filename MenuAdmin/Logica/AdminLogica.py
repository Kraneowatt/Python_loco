import pandas as pd
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar
from functools import partial

class AdminLogica:
    """
    Clase para manejar la lógica del administrador.
    """
    def __init__(self, conexion_base_datos):
        self.conexion_base_datos = conexion_base_datos

    def obtener_nombre_usuario(self, user_id):
        """
        Obtiene el nombre del administrador desde la base de datos.
        """
        conn = self.conexion_base_datos.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT nombre FROM Usuario WHERE idUsuario = ?", (user_id,))
                result = cursor.fetchone()
                return result[0] if result else "Desconocido"
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo obtener el nombre: {e}")
            finally:
                self.conexion_base_datos.cerrar_conexion()
        return "Desconocido"

    def obtener_fecha_actual(self):
        """
        Devuelve la fecha actual formateada.
        """
        return datetime.now().strftime("%d/%m/%Y")

    def abrir_gestion_dataset(self,root):
        gestion_window = tk.Toplevel(root)
        gestion_window.title("Good Airs - Dataset Dashboard")
        gestion_window.geometry("800x600")
        gestion_window.config(bg="#e6e6e6")
        main_frame = tk.Frame(gestion_window, bg="#e6e6e6")
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        title_label = tk.Label(main_frame, text="Gestión del Dataset", font=("Arial", 20, "bold"), bg="#e6e6e6")
        title_label.grid(row=0, columnspan=2, pady=10)
        labels = [
                ("Fecha", None),
                ("Temperatura Máxima", tk.Entry(main_frame)),
                ("Temperatura Mínima", tk.Entry(main_frame)),
                ("Temperatura Media", tk.Entry(main_frame)),
                ("Presión", tk.Entry(main_frame)),
                ("Precipitación", tk.Entry(main_frame)),
                ("Humedad Relativa", tk.Entry(main_frame)),
                ("Viento-Max Intensidad", tk.Entry(main_frame)),
                ("Viento-Med Intensidad", tk.Entry(main_frame))
                ]
        input_fields = {}
        for idx, (label_text, widget) in enumerate(labels, start=1):
                label = tk.Label(main_frame, text=label_text, font=("Arial", 12), bg="#e6e6e6")
                label.grid(row=idx, column=0, pady=5, sticky="w")
                if label_text == "Fecha":
                    input_field = tk.Entry(main_frame)
                    input_field.grid(row=idx, column=1, pady=5, padx=10, sticky="ew")
                    input_fields["Fecha"] = input_field
                    date_button = tk.Button(main_frame, text="Seleccionar Fecha", command=partial(self.select_date,input_fields), bg="#add8e6", font=("Arial", 10))
                    date_button.grid(row=idx, column=2, pady=5, padx=5)
                    
                else:
                    widget.grid(row=idx, column=1, pady=5, padx=10, sticky="ew")
                    input_fields[label_text] = widget
                    buttons = [
                        ("Consultar Dataset", "#ff6347"),  # Rojo tomate
                        ("Insertar Nuevos Datos al Dataset", "#ff7f50"),  # Coral
                        ("Consultar Dataset Normalizado", "#1e90ff"),  # Azul dodger
                        ("Entrenar red neuronal", "#ff8c00")  # Naranja
                        ]
                    button_functions = [
                        """consultar_dataset,
                        insertar_nuevos_datos,
                        ver_dataset_normalizado,
                        entrenar_red_neuronal"""
                        ]
                    for idx, (button_text, color) in enumerate(buttons, start=11):
                        button = tk.Button(main_frame, text=button_text, bg=color, font=("Arial", 12), command=button_functions[idx-11])
                        button.grid(row=idx, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    def abrir_notificaciones(self):
        """
        Abre la ventana de notificaciones (placeholder).
        """
        messagebox.showinfo("Notificaciones", "Funcionalidad en desarrollo.")

    def select_date(self, input_fields):
        def grab_date():
                selected_date = cal.get_date()
                input_fields["Fecha"].delete(0, tk.END)
                input_fields["Fecha"].insert(0, selected_date)
                calendar_window.destroy()
                
        calendar_window = tk.Toplevel()
        calendar_window.title("Seleccionar Fecha")
        cal = Calendar(calendar_window, selectmode='day', date_pattern='mm/dd/yyyy')
        cal.pack(pady=10)
        select_date_button = tk.Button(calendar_window, text="Seleccionar", command=grab_date)
        select_date_button.pack(pady=5)