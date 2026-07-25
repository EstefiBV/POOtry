import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 1")
ventana.geometry("400x200")

mensaje = tk.Label(ventana, text="Hola mundo", font=("Arial", 16))
mensaje.pack(pady=50)

ventana.mainloop()