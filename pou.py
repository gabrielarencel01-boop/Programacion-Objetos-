import tkinter as tk 
from PIL import Image, ImageTk
def boton_clic():
    print("Hiciste Click!")

def actualizar_etiqueta():
    nuevo_texto = entrada.get()
    etiqueta.config(text=nuevo_texto)
    
ventana = tk.Tk()
ventana.title("Mip primera aplicacion con Tkinter")
ventana.geometry("1600x500")
etiqueta = tk.Label(ventana,text="Hola,Grupo de programacion basica",
    font=("Arial",14, "bold"), fg="black", bg="pink",padx=20,pady=10)
etiqueta.pack()    
ventana.title("mi segunda etiqueta")
ventana.geometry("1600x500")
etiqueta2= tk.Label(ventana,text="Hola mi nombre es Gabriela",
    font=("Arial",14, "bold"), fg="black", bg="sky blue",padx=20,pady=10)
etiqueta2.pack()    
ventana.title("mi tercera etiqueta")
ventana.geometry("1600x500")
etiqueta3= tk.Label(ventana,text="Me encantan los elotes",
    font=("Arial",14, "bold"), fg="black", bg="pink",padx=20,pady=10)
etiqueta3.pack()    
ventana.title("mi cuarta etiqueta")
ventana.geometry("1600x500")
etiqueta3= tk.Label(ventana,text="Me gusta Lana del Rey",
    font=("Arial",14, "bold"), fg="black", bg="sky blue",padx=20,pady=10)
etiqueta3.pack()    

imagen = Image.open("pou.png")
imagen = imagen.resize((400,200))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack(pady=20)

boton = tk.Button(ventana, text="Haz clic aqui", command=boton_clic,font=("comic sans",30))
boton.pack(pady=20)

entrada = tk.Entry(ventana, width=60)
entrada.pack(pady=10)

boton2= tk.Button(ventana, text="Actualizar", command=actualizar_etiqueta)
boton2.pack()

etiqueta = tk.Label(ventana, text="Texto inicial", font=("Arial",12))
etiqueta.pack(pady=10)
ventana.mainloop()
