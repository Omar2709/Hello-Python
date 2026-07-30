import tkinter as tk
from tkinter import simpledialog, messagebox

# Ocultar la ventana principal de Tkinter
root = tk.Tk()
root.withdraw()

# Mostrar la ventana de diálogo para pedir texto
respuesta = simpledialog.askstring("Saludo", "¿Cómo te llamas?")

if respuesta is None:
    messagebox.showinfo("Resultado", "El usuario canceló la acción.")
elif respuesta.strip() == "":
    messagebox.showwarning("Resultado", "No escribiste ningún nombre.")
else:
    messagebox.showinfo("Saludo", f"Hola, {respuesta.strip()}")

root.destroy()