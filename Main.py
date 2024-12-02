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

def abrir_menu_principal():
    """
    Función para abrir la ventana principal y seleccionar el tipo de usuario.
    """
    root = tk.Tk()
    root.title("Good Airs")
    root.geometry("400x300")
    root.config(bg="#f2f2f2")

    def abrir_admin():
        # Conectar con la base de datos
        conexion_bd = ConexionBaseDatos('ODBC Driver 17 for SQL Server', 'DESKTOP-ERHEOKF\SQLEXPRESS', 'Hola')
        admin_soporte=AdminSoporte(conexion_bd)
        admin_logica = AdminLogica(conexion_bd,admin_soporte)
        admin_interfaz = AdminInterfaz(root, admin_logica)
        admin_interfaz.mostrar_dashboard(1)  # ID de ejemplo para el administrador

    def abrir_usuario():
        # Conectar con la base de datos
        conexion_bd = ConexionBaseDatos('ODBC Driver 17 for SQL Server', 'localhost', 'GoodAirs')
        usuario_logica = UsuarioLogica(conexion_bd)
        usuario_interfaz = UsuarioInterfaz(root, usuario_logica)
        usuario_interfaz.mostrar_dashboard(1)  # ID de ejemplo para el usuario

    def abrir_invitado():
        # Cargar el modelo y dataset para el invitado
        invitado_logica = InvitadoLogica(r"C:/Users/HP OMEN/Desktop/GoodAirs/Python_loco/datasets/UnBuenDataset.csv", 
                                         "C:/Users/HP OMEN/Desktop/GoodAirs/Python_loco/modelos/modelo_clima_dia_siguiente.keras")
        invitado_interfaz = InvitadoInterfaz(root, invitado_logica)
        invitado_interfaz.mostrar_ventana()

    # Botones para elegir el tipo de usuario
    btn_admin = tk.Button(root, text="Entrar como Administrador", command=abrir_admin, bg="#4CAF50", fg="white", font=("Arial", 12))
    btn_admin.pack(pady=10)

    btn_usuario = tk.Button(root, text="Entrar como Usuario", command=abrir_usuario, bg="#2196F3", fg="white", font=("Arial", 12))
    btn_usuario.pack(pady=10)

    btn_invitado = tk.Button(root, text="Entrar como Invitado", command=abrir_invitado, bg="#FF9800", fg="white", font=("Arial", 12))
    btn_invitado.pack(pady=10)

    # Iniciar la ventana principal
    root.mainloop()

if __name__ == "__main__":
    abrir_menu_principal()