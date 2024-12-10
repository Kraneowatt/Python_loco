from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date, timedelta
import numpy as np
import pandas as pd
from tkinter import ttk
from functools import partial
from tensorflow.keras.models import load_model
from Main import Main
class UsuarioLogica:
    """
    Clase para manejar la lógica del usuario.
    """
    def __init__(self, conexion_base_datos,UsuarioSoporte,dataset_path,model_path):
        self.conexion_base_datos = conexion_base_datos
        self.UsuarioSoporte=UsuarioSoporte
        self.dataset = pd.read_csv(dataset_path)
        self.model = load_model(model_path)
        self.interpretacion_salida = {
            "clima": {
                (0.67, 1): "SOLEADO",
                (0.34, 0.66): "NUBLADO",
                (0, 0.33): "LLUVIOSO",
            },
            "temperatura": {
                (0.67, 1): "CALIDO",
                (0.34, 0.66): "TEMPLADO",
                (0, 0.33): "FRIO",
            },
            "humedad": {
                (0.67, 1): "ALTA",
                (0.34, 0.66): "MEDIA",
                (0, 0.33): "BAJA",
            },
        }

    def obtener_nombre_usuario(self, user_id):
        """
        Obtiene el nombre del usuario desde la base de datos.
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

    def ver_datos_climaticos(self):
        """
        Lógica para mostrar los datos climáticos.
        """
        # Aquí podrías cargar los datos desde la base de datos o archivo
        messagebox.showinfo("Datos Climáticos", "Aquí se mostrarían los datos climáticos.")

    def realizar_encuesta(self,user_id):
        if (self.UsuarioSoporte.verificar_encuesta(user_id)):
            survey_window = tk.Toplevel()
            survey_window.title("Encuesta Diaria")
            survey_window.geometry("400x300")
            
            eficacia_var = tk.StringVar()
            precision_var = tk.StringVar()
            interaccion_var = tk.StringVar()
            comentario_var = tk.StringVar()

            tk.Label(survey_window, text="Eficacia (1-5):", font=("Arial", 10)).pack(pady=5)
            tk.Entry(survey_window, textvariable=eficacia_var).pack(pady=5)
            tk.Label(survey_window, text="Precisión (1-5):", font=("Arial", 10)).pack(pady=5)
            tk.Entry(survey_window, textvariable=precision_var).pack(pady=5)
            tk.Label(survey_window, text="Interacción (1-5):", font=("Arial", 10)).pack(pady=5)
            tk.Entry(survey_window, textvariable=interaccion_var).pack(pady=5)
            tk.Label(survey_window, text="Comentario:", font=("Arial", 10)).pack(pady=5)
            tk.Entry(survey_window, textvariable=comentario_var).pack(pady=5)
            tk.Button(survey_window, text="Enviar Encuesta", command=partial(self.submit_survey,eficacia_var,precision_var,interaccion_var,comentario_var,user_id,survey_window)).pack(pady=10)

        
        

    def submit_survey(self,eficacia_var,precision_var,interaccion_var,comentario_var,user_id,root):
            try:
                eficacia = int(eficacia_var.get())
                precision = int(precision_var.get())
                interaccion = int(interaccion_var.get())
                comentario = comentario_var.get()
                self.UsuarioSoporte.hacer_encuesta(user_id,eficacia,precision,interaccion,comentario,root)
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar la encuesta: {e}")
                tk.Button(root, text="Enviar Encuesta", command=self.submit_survey).pack(pady=10)


#Trivia 

    def trivia(self):
        trivia_window = tk.Toplevel()
        trivia_window.title("Trivia")
        trivia_window.geometry("400x300")
        trivia_window.config(bg="#f2f2f2")  # Fondo color claro

    # Título de la ventana
        tk.Label(trivia_window, text="Trivia - Acciones", font=("Arial", 14, "bold"), bg="#f2f2f2").pack(pady=10)

    # Función para cada botón (puedes personalizar lo que hagan)
        
        

    # Botones para las opciones
        tk.Button(trivia_window, text="Consejo de Verano", command=self.show_summer_advice, 
                bg="#4CAF50", fg="white", width=20).pack(pady=5)

        tk.Button(trivia_window, text="Día Más Frío", command=self.show_coldest_day, 
                bg="#2196F3", fg="white", width=20).pack(pady=5)

        tk.Button(trivia_window, text="Día Más Caluroso", command=self.show_hottest_day, 
                bg="#FFC107", fg="white", width=20).pack(pady=5)

        tk.Button(trivia_window, text="Consultar Dataset Público", command=self.show_public_dataset, 
                bg="#9C27B0", fg="white", width=20).pack(pady=5)
        
    def show_summer_advice(self):
                messagebox.showinfo("Consejo de Verano", "Recuerda mantenerte hidratado y usar protector solar.")

    def show_coldest_day(self):
        messagebox.showinfo("Día Más Frío", "El día más frío del año ocurrió el 15 de enero.")

    def show_hottest_day(self):
        messagebox.showinfo("Día Más Caluroso", "El día más caluroso del año fue el 10 de julio.")

    def show_public_dataset(self):
        file_path = r"C:\Users\proje\Desktop\GoodAirs\GestionAdmin\DatasetAdminGest.csv"
        try:
            df = pd.read_csv(file_path, sep=',', encoding='utf-8')
            dataset_window = tk.Toplevel()
            dataset_window.title("Consultar Dataset Público")
            dataset_window.geometry("1200x600")  # Ventana más ancha para mejor visualización
            dataset_window.config(bg="#f2f2f2")

    # Crear frame principal con padding
            main_frame = tk.Frame(dataset_window, bg="#f2f2f2")
            main_frame.pack(expand=True, fill="both", padx=20, pady=10)

    # Crear frame para el Treeview y scrollbars
            tree_frame = tk.Frame(main_frame)
            tree_frame.pack(expand=True, fill="both")

    # Crear Treeview con estilo personalizado
            style = ttk.Style()
            style.configure("Treeview", font=('Arial', 10))
            style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

            tree = ttk.Treeview(tree_frame, columns=list(df.columns), show="headings", style="Treeview")

    # Configurar scrollbars
            vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Configurar headers y columnas
            for column in df.columns:
                tree.heading(column, text=column, anchor="center")
        # Calcular el ancho máximo necesario para la columna
                max_width = max(
                    len(str(column)),  # Ancho del header
                    df[column].astype(str).str.len().max(),  # Ancho máximo de los datos
                    10  # Ancho mínimo
                ) * 10  # Multiplicar por 10 para obtener píxeles aproximados
                tree.column(column, width=max_width, minwidth=50, anchor="center")

            for idx, row in df.iterrows():
                formatted_row = []
                for value in row:
                    # Formatear números con 2 decimales si son float
                    if isinstance(value, float):
                        formatted_value = f"{value:.2f}"
                    else:
                        formatted_value = str(value)
                    formatted_row.append(formatted_value)
                tree.insert("", "end", values=formatted_row)

    # Colocar Treeview y scrollbars
            tree.grid(row=0, column=0, sticky="nsew")
            vsb.grid(row=0, column=1, sticky="ns")
            hsb.grid(row=1, column=0, sticky="ew")

    # Configurar grid weights
            tree_frame.grid_rowconfigure(0, weight=1)
            tree_frame.grid_columnconfigure(0, weight=1)

    # Botón para cerrar con estilo mejorado
            close_btn = tk.Button(
                dataset_window,
                text="Cerrar",
                command=dataset_window.destroy,
                bg="#4a90e2",
                fg="white",
                font=('Arial', 10, 'bold'),
                padx=20,
                pady=5,
                relief="flat"
            )
            close_btn.pack(pady=15)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        
#Notificaciones
    def open_notifications(self,user_id):
        notif_window = tk.Toplevel()
        notif_window.title("Notificaciones")
        notif_window.geometry("400x300")
        tk.Label(notif_window, text="Ventana de Notificaciones", font=("Arial", 12)).pack()
        self.UsuarioSoporte.mostrar_encuesta(notif_window,user_id)
        


#Ajustes

    def open_settings(self,user_id):
        settings_window = tk.Toplevel()
        settings_window.title("Ajustes")
        settings_window.geometry("500x700")  # Aumentado el tamaño para los nuevos campos
        settings_window.config(bg="#f2f2f2")

        # Obtener información actualizada del usuario
        current_name,current_username=self.UsuarioSoporte.obtener_info(user_id)

        settings_frame = tk.Frame(settings_window, bg="#f2f2f2")
        settings_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título y nombre actual
        tk.Label(settings_frame, text="Ajustes de Usuario", 
                font=("Arial", 14, "bold"), bg="#f2f2f2").pack(pady=10)
        
        # Sección de cambio de nombre
        tk.Label(settings_frame, text="Cambiar Nombre", 
                font=("Arial", 12, "bold"), bg="#f2f2f2").pack(pady=5)
        tk.Label(settings_frame, text=f"Nombre actual: {current_name}", 
                bg="#f2f2f2").pack(pady=5)
        entry_new_name = tk.Entry(settings_frame, width=30)
        entry_new_name.pack(pady=5)

        tk.Button(settings_frame, text="Cambiar Nombre", 
                 command=partial(self.change_name,user_id,entry_new_name,settings_window), bg="#4CAF50", fg="white", width=20).pack(pady=5)

        # Sección de cambio de nombre de usuario
        tk.Label(settings_frame, text="\nCambiar Nombre de Usuario", 
                font=("Arial", 12, "bold"), bg="#f2f2f2").pack(pady=5)
        tk.Label(settings_frame, text=f"Username actual: {current_username}", 
                bg="#f2f2f2").pack(pady=5)
        entry_new_username = tk.Entry(settings_frame, width=30)
        entry_new_username.pack(pady=5)

        

        tk.Button(settings_frame, text="Cambiar Username", 
                 command=partial(self.change_username,user_id,entry_new_username,settings_window), bg="#4CAF50", fg="white", width=20).pack(pady=5)

        # Sección de cambio de contraseña
        tk.Label(settings_frame, text="\nCambiar Contraseña", 
                font=("Arial", 12, "bold"), bg="#f2f2f2").pack(pady=5)
        
        tk.Label(settings_frame, text="Contraseña actual:", bg="#f2f2f2").pack(pady=2)
        entry_current_password = tk.Entry(settings_frame, show="*", width=30)
        entry_current_password.pack(pady=2)

        tk.Label(settings_frame, text="Nueva contraseña:", bg="#f2f2f2").pack(pady=2)
        entry_new_password = tk.Entry(settings_frame, show="*", width=30)
        entry_new_password.pack(pady=2)

        tk.Label(settings_frame, text="Confirmar nueva contraseña:", bg="#f2f2f2").pack(pady=2)
        entry_confirm_password = tk.Entry(settings_frame, show="*", width=30)
        entry_confirm_password.pack(pady=2)


        tk.Button(settings_frame, text="Cambiar Contraseña", 
                 command=partial(self.change_password,user_id,entry_current_password,entry_new_password,entry_confirm_password,settings_window), bg="#4CAF50", fg="white", width=20).pack(pady=5)

        # Botón de volver
        tk.Button(settings_frame, text="Volver",
                 command=settings_window.destroy,
                 bg="#9E9E9E", fg="white", width=20).pack(pady=10)

    def change_name(self,user_id,entry_new_name,root):
        new_name = entry_new_name.get().strip()
        if new_name:
            if self.UsuarioSoporte.cambiar_nombre_usuario(user_id, new_name):
                root.destroy()
                self.open_settings()  # Reabrir la ventana de ajustes actualizada

    def change_username(self,user_id,entry_new_username,root):
        new_username = entry_new_username.get().strip()
        if new_username:
            if self.UsuarioSoporte.cambiar_username(user_id, new_username):
                root.destroy()
                self.open_settings()
    
    def change_password(self,user_id,entry_current_password,entry_new_password,entry_confirm_password,root):
            current_password = entry_current_password.get().strip()
            new_password = entry_new_password.get().strip()
            confirm_password = entry_confirm_password.get().strip()

            if not all([current_password, new_password, confirm_password]):
                messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
                return

            if new_password != confirm_password:
                messagebox.showwarning("Advertencia", "Las nuevas contraseñas no coinciden.")
                return

            if self.UsuarioSoporte.cambiar_contraseña(user_id, current_password, new_password):
                root.destroy()
                messagebox.showinfo("Éxito", "Se recomienda volver a iniciar sesión.")
    

    
    def interpretar_valor(self, valor, interpretacion):
        """
        Función para interpretar valores normalizados en categorías.
        """
        valor = max(0, min(1, valor))  # Aseguramos que el valor esté en el rango [0, 1]
        for rango, etiqueta in interpretacion.items():
            if rango[0] <= valor <= rango[1]:
                return etiqueta
        return "FUERA DE RANGO"

    def predecir_clima(self, entrada):
        """
        Predice el clima para el día siguiente usando el modelo y datos de entrada.
        """
        entrada = np.array(list(entrada.values())).reshape(1, -1)  # Convertir entrada a formato aceptado por el modelo
        prediccion = self.model.predict(entrada)
        
        clima = self.interpretar_valor(prediccion[0][0], self.interpretacion_salida["clima"])
        temperatura = self.interpretar_valor(prediccion[0][1], self.interpretacion_salida["temperatura"])
        humedad = self.interpretar_valor(prediccion[0][2], self.interpretacion_salida["humedad"])
        
        return clima, temperatura, humedad, prediccion[0]

    def mostrar_prediccion(self):
        """
        Obtiene y muestra la predicción del clima para el invitado.
        """
        ultimo_registro = self.dataset.iloc[-1]
        entrada = {
            "temperatura_maxima": ultimo_registro["temperatura_maxima"],
            "temperatura_minima": ultimo_registro["temperatura_minima"],
            "temperatura_media": ultimo_registro["temperatura_media"],
            "presion": ultimo_registro["presion"],
            "precipitacion": ultimo_registro["precipitacion"],
            "humedad_relativa": ultimo_registro["humedad_relativa"],
            "vientomax_intensidad": ultimo_registro["vientomax_intensidad"],
            "vientomed_intensidad": ultimo_registro["vientomed_intensidad"]
        }

        clima, temperatura, humedad, valores_normalizados = self.predecir_clima(entrada)

        detalles = (
            f"Predicción para mañana:\n"
            f"Clima: {clima} ({valores_normalizados[0]:.2f})\n"
            f"Temperatura: {temperatura} ({valores_normalizados[1]:.2f})\n"
            f"Humedad: {humedad} ({valores_normalizados[2]:.2f})\n\n"
            f"Valores normalizados usados:\n"
            f"Temperatura máxima: {entrada['temperatura_maxima']:.2f}\n"
            f"Temperatura mínima: {entrada['temperatura_minima']:.2f}\n"
            f"Temperatura media: {entrada['temperatura_media']:.2f}\n"
            f"Presión: {entrada['presion']:.2f}\n"
            f"Precipitación: {entrada['precipitacion']:.2f}\n"
            f"Humedad relativa: {entrada['humedad_relativa']:.2f}\n"
            f"Viento máximo: {entrada['vientomax_intensidad']:.2f}\n"
            f"Viento medio: {entrada['vientomed_intensidad']:.2f}"
        )

        def cerrar_sesion(self,root):
            root.destroy
            main=Main()
            main.abrir_menu_principal()