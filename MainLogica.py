import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# Intentar con la importación estándar
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date, timedelta
from functools import partial
import numpy as np
import pandas as pd
from MainSoporte import main_soporte

class mainlogica:
    def __init__(self):
        pass

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
        btn_register = tk.Button(register_window, text="Registrar", command=
                                 partial(self.register_user(entry_name, entry_username, entry_email, entry_password, entry_confirm_email, entry_confirm_password), bg="#4CAF50", fg="white", font=("Arial", 12)))
        btn_register.grid(row=7, column=0, columnspan=2, pady=20)

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
        btn_login = tk.Button(login_window, text="Iniciar Sesión", command=partial(main_soporte.login_user,entry_email,entry_password), bg="#4CAF50", fg="white", font=("Arial", 12))
        btn_login.pack(pady=10)

        # Botón de "Olvidé la contraseña"
        btn_forgot_password = tk.Button(login_window, text="Olvidaste la contraseña?", command=lambda: messagebox.showinfo("Info", "Funcionalidad en construcción"), bg="#FFC107", fg="white", font=("Arial", 10))
        btn_forgot_password.pack()

    def open_guest_window(self,root):
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


    def register_user(self,entry_name, entry_username, entry_email, entry_password, entry_confirm_email, entry_confirm_password):
        print("Register button clicked.")  # Mensaje de depuración para verificar si la función es llamada.
        name = entry_name.get()
        username = entry_username.get()
        email = entry_email.get()
        password = entry_password.get()
        confirm_email = entry_confirm_email.get()
        confirm_password = entry_confirm_password.get()

        # Validaciones básicas
        if email != confirm_email:
            messagebox.showerror("Error", "Los correos no coinciden.")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres.")
            return
        
        mainlogica.register(self,name,username,email,password)


        # Comprobar si el usuario ya existe

def show_predictionguest(self):
    dataset = pd.read_csv("C:/Users/HP OMEN/Desktop/GoodAirs/Python_loco/datasets/DatasetAdminGest.csv")
    ultimo_registro = dataset.iloc[-1]
    
    # Crear un diccionario con los valores de entrada del último registro
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
    
    # Obtener predicción
    clima, temperatura, humedad, valores_normalizados = predecir_clima(entrada)
    
    # Crear descripción detallada de la predicción (valores normalizados)
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
    messagebox.showinfo("Predicción", detalles)

    def predecir_clima(self,entrada):
        interpretacion_salida = {
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
        entrada = np.array(list(entrada.values())).reshape(1, -1)  # Convertir entrada a formato aceptado por el modelo
        
        # Hacer la predicción
        prediccion = model.predict(entrada)
        
        # Interpretar la predicción, ajustando los valores si es necesario
        clima = interpretar_valor(prediccion[0][0], interpretacion_salida["clima"])
        temperatura = interpretar_valor(prediccion[0][1], interpretacion_salida["temperatura"])
        humedad = interpretar_valor(prediccion[0][2], interpretacion_salida["humedad"])
        
        return clima, temperatura, humedad, prediccion[0]
    
    def interpretar_valor(self,valor, interpretacion):
        # Aseguramos que el valor esté en el rango [0, 1]
        valor = max(0, min(1, valor))  # Ajuste para que el valor esté entre 0 y 1
        
        # Ahora buscar el rango adecuado para devolver la etiqueta
        for rango, etiqueta in interpretacion.items():
            if rango[0] <= valor <= rango[1]:
                return etiqueta
        # Si no cae en ningún rango, devolvemos un valor por defecto
        return "FUERA DE RANGO"
