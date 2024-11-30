from tkinter import messagebox

def validar_fecha(fecha_str):
    """
    Valida si la fecha proporcionada es válida según el formato mm/dd/yyyy.
    """
    try:
        datetime.strptime(fecha_str, "%m/%d/%Y")
        return True
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha incorrecto. Debe ser MM/DD/YYYY.")
        return False

def normalizar_datos(df, columnas):
    """
    Normaliza los datos de las columnas especificadas en el DataFrame.
    """
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    try:
        df[columnas] = scaler.fit_transform(df[columnas])
        return df
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo normalizar los datos: {e}")
        return None

def guardar_datos_csv(df, file_path):
    """
    Guarda un DataFrame a un archivo CSV.
    """
    try:
        df.to_csv(file_path, sep=',', index=False, encoding='utf-8')
        messagebox.showinfo("Éxito", "Los datos han sido guardados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

