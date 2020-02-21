import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

ventana = tk.Tk()
ventana.title("Sistema Escolar")

def impresion():
    registro3 = tk.Tk()
    registro3.title("Datos de registro.")
    textor=ttk.Label(registro3, text="Nombre: "+nombre.get()+" "+apellido1.get()+" "+apellido2.get())
    textor.grid(column=0, row=0)
    textor2=ttk.Label(registro3, text="Direccion: "+direccion.get())
    textor2.grid(column=0, row=1)
    textor3=ttk.Label(registro3, text=colonia.get())
    textor3.grid(column=0, row=2)
    textor4=ttk.Label(registro3, text="Ciudad: "+ciudad.get())
    textor4.grid(column=0, row=3)
    textor5=ttk.Label(registro3, text="Municipio: "+muni.get())
    textor5.grid(column=0, row=4)

    textov=ttk.Label(registro3, text="Pasatiempos: ")
    textov.grid(column=0, row=5)

    if opcion_1.get()==1:
        texto_c=ttk.Label(registro3, text="* Te gustan los Videojuegos.")
        texto_c.grid(column=0, row=6)
    else:
        texto_c=ttk.Label(registro3, text="* No te gustan los Videojuegos.")
        texto_c.grid(column=0, row=6)
    if opcion_2.get()==1:
        texto_x=ttk.Label(registro3, text="* Te gustan los Deportes.")
        texto_x.grid(column=0, row=7)
    else:
        texto_x=ttk.Label(registro3, text="* No te gustan los Deportes.")
        texto_x.grid(column=0, row=7)
    if opcion_3.get()==1:
        texto_a=ttk.Label(registro3, text="* Te gustan las Artes.")
        texto_a.grid(column=0, row=8)
    else:
        texto_a=ttk.Label(registro3, text="* No te gustan las Artes.")
        texto_a.grid(column=0, row=8)
    if opcion_4.get()==1:
        texto_z=ttk.Label(registro3, text="* Te gusta ver Series.")
        texto_z.grid(column=0, row=9)
    else:
        texto_z=ttk.Label(registro3, text="* No te gusta ver Series.")
        texto_z.grid(column=0, row=9)
    if opcion_5.get()==1:
        texto_h=ttk.Label(registro3, text="* Te gusta Chismear.")
        texto_h.grid(column=0, row=10)
    else:
        texto_h=ttk.Label(registro3, text="* No te gusta Chismear.")
        texto_h.grid(column=0, row=10)
    if opcion_6.get()==1:
        texto_h=ttk.Label(registro3, text="* Te gusta Cocinar.")
        texto_h.grid(column=0, row=11)
    else:
        texto_h=ttk.Label(registro3, text="* No te gusta Cocinar.")
        texto_h.grid(column=0, row=11)

    textod=ttk.Label(registro3, text="Estado civil: ")
    textod.grid(column=0, row=12)
    if opcion.get()==1:
        textod=ttk.Label(registro3, text="* Soltero / Soltera.")
        textod.grid(column=0, row=13)
    if opcion.get()==2:
        textod=ttk.Label(registro3, text="* Casado / Casada.")
        textod.grid(column=0, row=13)
    if opcion.get()==3:
        textod=ttk.Label(registro3, text="* Divorciado / Divorciada.")
        textod.grid(column=0, row=13)
    if opcion.get()==4:
        textod=ttk.Label(registro3, text="* Viudo / Viuda.")
        textod.grid(column=0, row=13)
    if opcion.get()==5:
        textod=ttk.Label(registro3, text="* Abandonado / Abandonada.")
        textod.grid(column=0, row=13)
    if opcion.get()==6:
        textod=ttk.Label(registro3, text="* No lo sabes.")
        textod.grid(column=0, row=13)
    if caja.get('1.0', 'end-1c')!="":
        ttk.Label(registro3, text="Objetivo en la vida:\n"+caja.get('1.0', 'end-1c')).grid(column=0, row=14)
    else:
        ttk.Label(registro3, text="Objetivo en la vida:\n----").grid(column=0, row=14)
    textor3=ttk.Label(registro3, text="Registro hecho con exito")
    textor3.grid(column=0, row=15)
    textor3.configure(foreground="green")

def funcion_imprimir():
    if opcion.get()==0 or nombre.get()=="" or apellido1.get()=="" or apellido2.get()=="" or direccion.get()=="":
        mBox.showwarning('Error al imprimir.',
    'Datos Incompletos.\nFavor de llenar los requisitos de las ventanas.')
    else:
        impresion()

def funcion_caja_mensaje():
    mBox.showinfo('Datos del creador.',
    'Nombre: Francisco Javier Herrejon Mendoza\nCarrera: I.S.C.\nSemestre: Cuarto\nCompañia: FJ,s')

def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

def registrado():
    registro = tk.Tk()
    registro.title("Datos de registro.")
    textor=ttk.Label(registro, text="Nombre: "+nombre.get()+" "+apellido1.get()+" "+apellido2.get())
    textor.grid(column=1, row=0)
    textor2=ttk.Label(registro, text="Direccion: "+direccion.get())
    textor2.grid(column=1, row=1)
    textor3=ttk.Label(registro, text=colonia.get())
    textor3.grid(column=1, row=2)
    textor4=ttk.Label(registro, text="Ciudad: "+ciudad.get())
    textor4.grid(column=1, row=3)
    textor5=ttk.Label(registro, text="Municipio: "+muni.get())
    textor5.grid(column=1, row=4)
    textor3=ttk.Label(registro, text="Registro hecho con exito")
    textor3.grid(column=1, row=5)
    textor3.configure(foreground="green")

def clickMe():
    textof=ttk.Label(tab1, text="")
    textof.grid(column=1, row=8)
    if nombre.get()=="" or apellido1.get()=="" or apellido2.get()=="" or direccion.get()=="":
        textof.configure(text="Datos incompletos.")
        textof.configure(foreground='red')
    else:
        textof.configure(text="  Datos completos.  ")
        textof.configure(foreground='green')
        accion.configure(text="Registrado")
        registrado()

def funciones():
    registro2 = tk.Tk()
    registro2.title("Datos de registro.")

    textof=ttk.Label(registro2, text="Hola "+nombre.get()+" "+apellido1.get()+" "+apellido2.get())
    textof.grid(column=0, row=0)
    textov=ttk.Label(registro2, text="Pasatiempos: ")
    textov.grid(column=0, row=1)

    if opcion_1.get()==1:
        texto_c=ttk.Label(registro2, text="* Te gustan los Videojuegos.")
        texto_c.grid(column=0, row=2)
    else:
        texto_c=ttk.Label(registro2, text="* No te gustan los Videojuegos.")
        texto_c.grid(column=0, row=2)
    if opcion_2.get()==1:
        texto_x=ttk.Label(registro2, text="* Te gustan los Deportes.")
        texto_x.grid(column=0, row=3)
    else:
        texto_x=ttk.Label(registro2, text="* No te gustan los Deportes.")
        texto_x.grid(column=0, row=3)
    if opcion_3.get()==1:
        texto_a=ttk.Label(registro2, text="* Te gustan las Artes.")
        texto_a.grid(column=0, row=4)
    else:
        texto_a=ttk.Label(registro2, text="* No te gustan las Artes.")
        texto_a.grid(column=0, row=4)
    if opcion_4.get()==1:
        texto_z=ttk.Label(registro2, text="* Te gusta ver Series.")
        texto_z.grid(column=0, row=5)
    else:
        texto_z=ttk.Label(registro2, text="* No te gusta ver Series.")
        texto_z.grid(column=0, row=5)
    if opcion_5.get()==1:
        texto_h=ttk.Label(registro2, text="* Te gusta Chismear.")
        texto_h.grid(column=0, row=6)
    else:
        texto_h=ttk.Label(registro2, text="* No te gusta Chismear.")
        texto_h.grid(column=0, row=6)
    if opcion_6.get()==1:
        texto_h=ttk.Label(registro2, text="* Te gusta Cocinar.")
        texto_h.grid(column=0, row=7)
    else:
        texto_h=ttk.Label(registro2, text="* No te gusta Cocinar.")
        texto_h.grid(column=0, row=7)

    textod=ttk.Label(registro2, text="Estado civil: ")
    textod.grid(column=0, row=9)
    if opcion.get()==1:
        textod=ttk.Label(registro2, text="* Soltero / Soltera.")
        textod.grid(column=0, row=10)
    if opcion.get()==2:
        textod=ttk.Label(registro2, text="* Casado / Casada.")
        textod.grid(column=0, row=10)
    if opcion.get()==3:
        textod=ttk.Label(registro2, text="* Divorciado / Divorciada.")
        textod.grid(column=0, row=10)
    if opcion.get()==4:
        textod=ttk.Label(registro2, text="* Viudo / Viuda.")
        textod.grid(column=0, row=10)
    if opcion.get()==5:
        textod=ttk.Label(registro2, text="* Abandonado / Abandonada.")
        textod.grid(column=0, row=10)
    if opcion.get()==6:
        textod=ttk.Label(registro2, text="* No lo sabes.")
        textod.grid(column=0, row=10)
    if caja.get('1.0', 'end-1c')!="":
        ttk.Label(registro2, text="Objetivo en la vida:\n"+caja.get('1.0', 'end-1c')).grid(column=0, row=12)
    else:
        ttk.Label(registro2, text="Objetivo en la vida:\n----").grid(column=0, row=12)
    textou=ttk.Label(registro2, text="Registro hecho con exito")
    textou.grid(column=0, row=13)
    textou.configure(foreground='green')

def clickado():
    textop=ttk.Label(tab2, text="")
    textop.grid(column=1, row=11)

    if opcion.get()==0 or nombre.get()=="" or apellido1.get()=="" or apellido2.get()=="" or direccion.get()=="":
        textop.configure(text="Datos incompletos.")
        textop.configure(foreground='red')
    else:
        textop.configure(text="  Datos completos.  ")
        textop.configure(foreground='green')
        funciones()

tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text='Datos personales.')
tabControl.pack(expand=0, fill="both")
tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text='Datos extras.')

texto=ttk.Label(tab1, text="Captura de Alumnos")
texto.grid(column=1, row=0)

texto1=ttk.Label(tab1, text="\nNombre:   ")
texto1.grid(column=0, row=1)
nombre=tk.StringVar()
nombreCapturado = ttk.Entry(tab1, width=12, textvariable=nombre)
nombreCapturado.grid(column=1, row=1)

texto2=ttk.Label(tab1, text="\nApellido Paterno:   ")
texto2.grid(column=0, row=2)
apellido1=tk.StringVar()
apellido1Capturado = ttk.Entry(tab1, width=12, textvariable=apellido1)
apellido1Capturado.grid(column=1, row=2)

texto3=ttk.Label(tab1, text="\nApellido Materno:   ")
texto3.grid(column=0, row=3)
apellido2=tk.StringVar()
apellido2Capturado = ttk.Entry(tab1, width=12, textvariable=apellido2)
apellido2Capturado.grid(column=1, row=3)

texto4=ttk.Label(tab1, text="\nDireccion:   ")
texto4.grid(column=0, row=4)
direccion=tk.StringVar()
direccionCapturado = ttk.Entry(tab1, width=12, textvariable=direccion)
direccionCapturado.grid(column=1, row=4)

ttk.Label(tab1, text="\nColonia:   ").grid(column=0, row=5)
colonia=tk.StringVar()
coloniaSeleccionado = ttk.Combobox(tab1, width=15, textvariable=colonia)
coloniaSeleccionado['values']=("Col. Vicente Rivapalacio", "Col. Centro", "Col. Lago 1")
coloniaSeleccionado.grid(column=1, row=5)
coloniaSeleccionado.current(0)

ttk.Label(tab1, text="\nCiudad:   ").grid(column=0, row=6)
ciudad=tk.StringVar()
ciudadSeleccionado = ttk.Combobox(tab1, width=15, textvariable=ciudad)
ciudadSeleccionado['values']=("Michoacan", "Queretaro", "Guadalajara")
ciudadSeleccionado.grid(column=1, row=6)
ciudadSeleccionado.current(0)

ttk.Label(tab1, text="\nMunicipio:   ").grid(column=0, row=7)
muni=tk.StringVar()
muniSeleccionado = ttk.Combobox(tab1, width=15, textvariable=muni)
muniSeleccionado['values']=("Morelia", "Patzcuaro", "Zamora")
muniSeleccionado.grid(column=1, row=7)
muniSeleccionado.current(0)

accion=ttk.Button(tab1, text="Registrar", command=clickMe)
accion.grid(column=2, row=8)

ttk.Label(tab2, text="Datos Extras").grid(column=1, row=0)

ttk.Label(tab2, text="Pasatiempos:").grid(column=0, row=2)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(tab2, text="Videojuegos", variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=1, row=2, sticky=tk.W)

opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(tab2, text="Deportes", variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=2, row=2, sticky=tk.W)

opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(tab2, text="Artes", variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=3, row=2, sticky=tk.W)

opcion_4=tk.IntVar()
casilla_4=tk.Checkbutton(tab2, text="Ver Series", variable=opcion_4)
casilla_4.deselect()
casilla_4.grid(column=1, row=3, sticky=tk.W)

opcion_5=tk.IntVar()
casilla_5=tk.Checkbutton(tab2, text="Chismear", variable=opcion_5)
casilla_5.deselect()
casilla_5.grid(column=2, row=3, sticky=tk.W)

opcion_6=tk.IntVar()
casilla_6=tk.Checkbutton(tab2, text="Cocinar", variable=opcion_6)
casilla_6.deselect()
casilla_6.grid(column=3, row=3, sticky=tk.W)

ttk.Label(tab2, text="Estado civil:").grid(column=0, row=5)
opcion=tk.IntVar()
radio1=tk.Radiobutton(tab2, text="Soltero", variable=opcion, value=1)
radio1.grid(column=1, row=5, sticky=tk.W)

radio2=tk.Radiobutton(tab2, text="Casado", variable=opcion, value=2)
radio2.grid(column=2, row=5, sticky=tk.W)

radio3=tk.Radiobutton(tab2, text="Divorciado", variable=opcion, value=3)
radio3.grid(column=3, row=5, sticky=tk.W)

radio4=tk.Radiobutton(tab2, text="Viudo", variable=opcion, value=4)
radio4.grid(column=1, row=6, sticky=tk.W)

radio5=tk.Radiobutton(tab2, text="Abandonado", variable=opcion, value=5)
radio5.grid(column=2, row=6, sticky=tk.W)

radio6=tk.Radiobutton(tab2, text="No lo sé", variable=opcion, value=6)
radio6.grid(column=3, row=6, sticky=tk.W)

scrol_ancho=30
scrol_largo=5

ttk.Label(tab2, text="Objetivo de la vida: ").grid(column=0, row=8)
caja=scrolledtext.ScrolledText(tab2, width=scrol_ancho, height=scrol_largo, wrap=tk.WORD)
caja.grid(column=0, row=9)

botton2=ttk.Button(tab2, text="Registrar", command=clickado)
botton2.grid(column=2, row=10)

barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Imprimir", command=funcion_imprimir)
opciones_menu.add_separator()
opciones_menu.add_command(label="Salir", command=funcion_salir)
barra_menu.add_cascade(label="Sistema", menu=opciones_menu)

menu_ayuda=Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=funcion_caja_mensaje)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

nombreCapturado.focus()

ventana.mainloop()