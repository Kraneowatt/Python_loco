import tkinter as tk
from tkinter import messagebox

class InvitadoInterfaz:
    """
    Clase para manejar la interfaz gráfica para los invitados.
    """
    def __init__(self, root, invitado_logica):
        self.root = root
        self.invitado_logica = invitado_logica
