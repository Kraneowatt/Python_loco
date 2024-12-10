from tkinter import messagebox
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from Main import Main
class InvitadoLogica:
    """
    Clase para manejar la lógica de predicción y datos del invitado.
    """
    def __init__(self, dataset_path, model_path):
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

    def obtener_prediccion_invitado(self):
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

        return detalles

    def cerrar_sesion(self,root):
            root.destroy
            main=Main()
            main.abrir_menu_principal()