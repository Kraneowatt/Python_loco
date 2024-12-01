import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# Intentar con la importación estándar
import tkinter as tk
from tkinter import messagebox

from MenuUsuario.Logica.UsuarioLogica import UsuarioLogica
from MenuUsuario.Interfaz.UsuarioInterfaz import UsuarioInterfaz

from MenuAdmin.Logica.AdminLogica import AdminLogica
from MenuAdmin.Interfaz.AdminInterfaz import AdminInterfaz
from MenuAdmin.Soporte.AdminSoporte import AdminSoporte

from Invitado.Logica.InvitadoLogica import InvitadoLogica
from Invitado.Interfaz.InvitadoInterfaz import InvitadoInterfaz

from ConexionBaseDatos.BaseDatos import ConexionBaseDatos
from functools import partial

from MainLogica import mainlogica

class main:
     
    def __init__(self):
         pass
    def abrir_menu_principal():
            root = tk.Tk()
            root.title("Good Airs!")
            root.geometry("400x300")
            root.config(bg="#f2f2f2")  # Establecer el color de fondo para la ventana principal

            # Pantalla de bienvenida
            welcome_label = tk.Label(root, text="Bienvenido a Good Airs!\nInicie o Registrese para continuar!", font=("Arial", 14, "bold"), bg="#f2f2f2")
            welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

            # Botones de acción
            btn_register = tk.Button(root, text="Registrarse", command=partial(mainlogica.open_register_window,root), bg="#4CAF50", fg="white", font=("Arial", 12))
            btn_register.grid(row=1, column=0, pady=10)

            btn_login = tk.Button(root, text="Iniciar Sesión", command=partial(mainlogica.open_login_window,root), bg="#2196F3", fg="white", font=("Arial", 12))
            btn_login.grid(row=2, column=0, pady=10)

            btn_exit = tk.Button(root, text="Salir", command=root.quit, bg="#f44336", fg="white", font=("Arial", 12))
            btn_exit.grid(row=3, column=0, pady=10)

            # Botones de invitado
            guest_frame = tk.Frame(root, bg="#f2f2f2")
            guest_frame.grid(row=4, column=0, pady=10)

            guest_label = tk.Label(guest_frame, text="O bien.. entre como invitado.", bg="#f2f2f2", font=("Arial", 12))
            guest_label.grid(row=0, column=0, padx=5)

            btn_guest = tk.Button(guest_frame, text="Invitado", command=partial(mainlogica.open_guest_window,root), bg="#FF9800", fg="white", font=("Arial", 12))
            btn_guest.grid(row=0, column=1, padx=5)

            # Botón de información
            def show_info():
                messagebox.showinfo("Información", "Como invitado, tienes acceso limitado. No puedes dar feedback, pero puedes predecir.")

                btn_info = tk.Button(root, text="?", command=show_info, bg="#9E9E9E", fg="white", font=("Arial", 12))
                btn_info.place(x=20, y=20)

            # Ejecutar la aplicación
            root.mainloop()

    



    if __name__ == "__main__":
        abrir_menu_principal()
