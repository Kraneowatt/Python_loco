import pandas as pd
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar
from functools import partial
from tkinter import ttk
from tkinter import filedialog, messagebox, simpledialog

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
                        self.consultar_dataset,
                        self.insertar_nuevos_datos,
                        self.ver_dataset_normalizado,
                        self.entrenar_red_neuronal
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
    
    
    def consultar_dataset(self): 
        file_path = r"C:\Users\proje\Desktop\GoodAirs\GestionAdmin\DatasetAdminGest.csv"
        try:
            df = pd.read_csv(file_path, sep=',', encoding='utf-8')
            dataset_window = tk.Toplevel()
            dataset_window.title("Consultar Dataset")
            dataset_window.geometry("1200x600")
            dataset_window.config(bg="#f2f2f2")
            main_frame = tk.Frame(dataset_window, bg="#f2f2f2")
            main_frame.pack(expand=True, fill="both", padx=20, pady=10)
            tree_frame = tk.Frame(main_frame)
            tree_frame.pack(expand=True, fill="both")
            
            tree = ttk.Treeview(tree_frame, columns=list(df.columns), show="headings")
            vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            
            for column in df.columns:
                tree.heading(column, text=column, anchor="center")
                max_width = max(len(str(column)), df[column].astype(str).str.len().max(), 10) * 10
                tree.column(column, width=max_width, anchor="center")
            
            for _, row in df.iterrows():
                tree.insert("", "end", values=list(row))
                
                tree.grid(row=0, column=0, sticky="nsew")
                vsb.grid(row=0, column=1, sticky="ns")
                hsb.grid(row=1, column=0, sticky="ew")
                tree_frame.grid_rowconfigure(0, weight=1)
                tree_frame.grid_columnconfigure(0, weight=1)
                
                def borrar_dato(df):
                    id_a_borrar = simpledialog.askstring("Borrar Dato", "Ingrese la ID del dato a borrar:")
                    if id_a_borrar:
                        try:
                            id_a_borrar = int(id_a_borrar)
                            if id_a_borrar in df['id_dato'].values:
                                df = df[df['id_dato'] != id_a_borrar]
                                
                                df.to_csv(file_path, index=False, sep=',', encoding='utf-8')
                                
                                for item in tree.get_children():
                                    tree.delete(item)
                                for _, row in df.iterrows():
                                    tree.insert("", "end", values=list(row))
                                        
                                messagebox.showinfo("Éxito", f"Los datos con la ID {id_a_borrar} han sido eliminados.")
                            else:
                                messagebox.showerror("Error", "No se encontró la ID proporcionada.")
                        except ValueError:
                            messagebox.showerror("Error", "La ID debe ser un número entero.")
                        except Exception as e:
                            messagebox.showerror("Error", f"Hubo un problema al intentar borrar el dato: {e}")
                    else:
                        messagebox.showwarning("Advertencia", "Debe ingresar una ID válida.")

            borrar_button = tk.Button(dataset_window, text="Borrar Dato", command=lambda: borrar_dato(df), bg="#ff6347", font=("Arial", 12))
            borrar_button.pack(pady=10)
            
            tk.Button(dataset_window, text="Cerrar", command=dataset_window.destroy, bg="#ff6347", font=("Arial", 12)).pack(pady=10)
        
        except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

    def ver_dataset_normalizado():
            file_path = r"C:\Users\proje\Desktop\GoodAirs\GestionAdmin\UnBuenDataset.csv"
            try:
                df = pd.read_csv(file_path, sep=',', encoding='utf-8')
                dataset_window = tk.Toplevel()
                dataset_window.title("Consultar Dataset")
                dataset_window.geometry("1200x600")
                dataset_window.config(bg="#f2f2f2")
                main_frame = tk.Frame(dataset_window, bg="#f2f2f2")
                main_frame.pack(expand=True, fill="both", padx=20, pady=10)
                tree_frame = tk.Frame(main_frame)
                tree_frame.pack(expand=True, fill="both")
                
                tree = ttk.Treeview(tree_frame, columns=list(df.columns), show="headings")
                vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
                hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
                tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
                
                for column in df.columns:
                    tree.heading(column, text=column, anchor="center")
                    max_width = max(len(str(column)), df[column].astype(str).str.len().max(), 10) * 10
                    tree.column(column, width=max_width, anchor="center")
                
                for _, row in df.iterrows():
                    tree.insert("", "end", values=list(row))
                    
                    tree.grid(row=0, column=0, sticky="nsew")
                    vsb.grid(row=0, column=1, sticky="ns")
                    hsb.grid(row=1, column=0, sticky="ew")
                    tree_frame.grid_rowconfigure(0, weight=1)
                    tree_frame.grid_columnconfigure(0, weight=1)
                
                tk.Button(dataset_window, text="Cerrar", command=dataset_window.destroy, bg="#ff6347", font=("Arial", 12)).pack(pady=10)
            
            except Exception as e:
                    messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")  
    def insertar_nuevos_datos(self,input_fields):
            file_path = r"C:\Users\proje\Desktop\GoodAirs\GestionAdmin\DatasetAdminGest.csv"
            try:
                df = pd.read_csv(file_path, sep=',', encoding='utf-8')
                for key, field in input_fields.items():
                    if not field.get():
                        messagebox.showerror("Error", f"El campo '{key}' no puede estar vacío.")
                        return
                
                
                nueva_id = df['id_dato'].max() + 1
                
                fecha_str = input_fields["Fecha"].get()
                try:
                    fecha_obj = datetime.strptime(fecha_str, "%m/%d/%Y")
                    try:
                        fecha_formateada = fecha_obj.strftime("%-m/%-d/%Y")
                    except ValueError:
                        fecha_formateada = f"{fecha_obj.month}/{fecha_obj.day}/{fecha_obj.year}"
                    print("Fecha formateada", fecha_formateada)
                except ValueError:
                    messagebox.showerror("Error", "Formato de fecha incorrecto.")    
                
                nueva_fila = {
                    "id_dato": nueva_id,
                    "fecha": fecha_formateada,
                    "temperatura_maxima": float(input_fields["Temperatura Máxima"].get()),
                    "temperatura_minima": float(input_fields["Temperatura Mínima"].get()),
                    "temperatura_media": float(input_fields["Temperatura Media"].get()),
                    "presion": float(input_fields["Presión"].get()),
                    "precipitacion": float(input_fields["Precipitación"].get()),
                    "humedad_relativa": int(input_fields["Humedad Relativa"].get()),
                    "vientomax_intensidad": float(input_fields["Viento-Max Intensidad"].get()),
                    "vientomed_intensidad": float(input_fields["Viento-Med Intensidad"].get())
                    }
                
                nueva_fila_df = pd.DataFrame([nueva_fila])
                
                df = pd.concat([df, nueva_fila_df], ignore_index=True)
                
                df.to_csv(file_path, sep=',', index=False, encoding='utf-8')
                messagebox.showinfo("Éxito", f"Datos insertados correctamente con ID {nueva_id}.")
                
                for field in input_fields.values():
                    field.delete(0, tk.END)
            
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo insertar el dato: {e}")
        
    def entrenar_red_neuronal(self,root):
            progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
            progress.grid(row=0, column=0, pady=10, padx=10)
            progress.start()
                
            try:
                file_path = r'C:\Users\proje\Desktop\GoodAirs\GestionAdmin\entrenador.py'
                subprocess.run(['python', file_path], check=True)
                messagebox.showinfo("Entrenamiento completado", "El entrenamiento del modelo ha finalizado correctamente.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Ocurrió un error durante el entrenamiento: {e}")
            finally:
                progress.stop()
                progress.destroy()