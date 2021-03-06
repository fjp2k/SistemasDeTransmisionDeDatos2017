#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Nov 08, 2017 10:42:34 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import pantalla_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    pantalla_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    pantalla_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    pantalla_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    pantalla_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("922x493+479+253")
        top.title("New Toplevel 1")
        top.configure(background="#f1f1f1")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.labelServidorPop = Label(top)
        self.labelServidorPop.place(relx=0.01, rely=0.02, height=30, width=135)
        self.labelServidorPop.configure(activebackground="#f9f9f9")
        self.labelServidorPop.configure(activeforeground="black")
        self.labelServidorPop.configure(anchor=W)
        self.labelServidorPop.configure(background="#f1f1f1")
        self.labelServidorPop.configure(disabledforeground="#a3a3a3")
        self.labelServidorPop.configure(foreground="#000000")
        self.labelServidorPop.configure(highlightbackground="#d9d9d9")
        self.labelServidorPop.configure(highlightcolor="black")
        self.labelServidorPop.configure(text='''Servidor Pop:''')

        self.conectar_btn = Button(top)
        self.conectar_btn.place(relx=0.74, rely=0.02, height=70, width=105)
        self.conectar_btn.configure(activebackground="#d9d9d9")
        self.conectar_btn.configure(activeforeground="#000000")
        self.conectar_btn.configure(background="#d9d9d9")
        self.conectar_btn.configure(command=pantalla_support.conectar)
        self.conectar_btn.configure(disabledforeground="#a3a3a3")
        self.conectar_btn.configure(foreground="#000000")
        self.conectar_btn.configure(highlightbackground="#d9d9d9")
        self.conectar_btn.configure(highlightcolor="black")
        self.conectar_btn.configure(pady="0")
        self.conectar_btn.configure(text='''Conectar''')

        self.servidor_entry = Entry(top)
        self.servidor_entry.place(relx=0.16, rely=0.02, relheight=0.06
                , relwidth=0.19)
        self.servidor_entry.configure(background="white")
        self.servidor_entry.configure(disabledforeground="#a3a3a3")
        self.servidor_entry.configure(font="TkFixedFont")
        self.servidor_entry.configure(foreground="#000000")
        self.servidor_entry.configure(highlightbackground="#d9d9d9")
        self.servidor_entry.configure(highlightcolor="black")
        self.servidor_entry.configure(insertbackground="black")
        self.servidor_entry.configure(selectbackground="#c4c4c4")
        self.servidor_entry.configure(selectforeground="black")

        self.usuario_lb = Label(top)
        self.usuario_lb.place(relx=0.01, rely=0.1, height=30, width=135)
        self.usuario_lb.configure(activebackground="#f9f9f9")
        self.usuario_lb.configure(activeforeground="black")
        self.usuario_lb.configure(anchor=W)
        self.usuario_lb.configure(background="#f1f1f1")
        self.usuario_lb.configure(disabledforeground="#a3a3a3")
        self.usuario_lb.configure(foreground="#000000")
        self.usuario_lb.configure(highlightbackground="#d9d9d9")
        self.usuario_lb.configure(highlightcolor="black")
        self.usuario_lb.configure(text='''Usuario:''')

        self.puerto_lb = Label(top)
        self.puerto_lb.place(relx=0.38, rely=0.02, height=30, width=135)
        self.puerto_lb.configure(activebackground="#f9f9f9")
        self.puerto_lb.configure(activeforeground="black")
        self.puerto_lb.configure(anchor=W)
        self.puerto_lb.configure(background="#f1f1f1")
        self.puerto_lb.configure(disabledforeground="#a3a3a3")
        self.puerto_lb.configure(foreground="#000000")
        self.puerto_lb.configure(highlightbackground="#d9d9d9")
        self.puerto_lb.configure(highlightcolor="black")
        self.puerto_lb.configure(text='''Puerto(SSL):''')

        self.contrasenia_lb = Label(top)
        self.contrasenia_lb.place(relx=0.01, rely=0.18, height=30, width=135)
        self.contrasenia_lb.configure(activebackground="#f9f9f9")
        self.contrasenia_lb.configure(activeforeground="black")
        self.contrasenia_lb.configure(anchor=W)
        self.contrasenia_lb.configure(background="#f1f1f1")
        self.contrasenia_lb.configure(disabledforeground="#a3a3a3")
        self.contrasenia_lb.configure(foreground="#000000")
        self.contrasenia_lb.configure(highlightbackground="#d9d9d9")
        self.contrasenia_lb.configure(highlightcolor="black")
        self.contrasenia_lb.configure(text='''Contrasenia:''')

        self.frecuencia_lb = Label(top)
        self.frecuencia_lb.place(relx=0.01, rely=0.26, height=30, width=135)
        self.frecuencia_lb.configure(activebackground="#f9f9f9")
        self.frecuencia_lb.configure(activeforeground="black")
        self.frecuencia_lb.configure(anchor=W)
        self.frecuencia_lb.configure(background="#f1f1f1")
        self.frecuencia_lb.configure(disabledforeground="#a3a3a3")
        self.frecuencia_lb.configure(foreground="#000000")
        self.frecuencia_lb.configure(highlightbackground="#d9d9d9")
        self.frecuencia_lb.configure(highlightcolor="black")
        self.frecuencia_lb.configure(text='''Frecuencia(seg.):''')

        self.usuario_entry = Entry(top)
        self.usuario_entry.place(relx=0.16, rely=0.1, relheight=0.06
                , relwidth=0.19)
        self.usuario_entry.configure(background="white")
        self.usuario_entry.configure(disabledforeground="#a3a3a3")
        self.usuario_entry.configure(font="TkFixedFont")
        self.usuario_entry.configure(foreground="#000000")
        self.usuario_entry.configure(highlightbackground="#d9d9d9")
        self.usuario_entry.configure(highlightcolor="black")
        self.usuario_entry.configure(insertbackground="black")
        self.usuario_entry.configure(selectbackground="#c4c4c4")
        self.usuario_entry.configure(selectforeground="black")

        self.contrasenia_entry = Entry(top)
        self.contrasenia_entry.place(relx=0.16, rely=0.18, relheight=0.06
                , relwidth=0.19)
        self.contrasenia_entry.configure(background="white")
        self.contrasenia_entry.configure(disabledforeground="#a3a3a3")
        self.contrasenia_entry.configure(font="TkFixedFont")
        self.contrasenia_entry.configure(foreground="#000000")
        self.contrasenia_entry.configure(highlightbackground="#d9d9d9")
        self.contrasenia_entry.configure(highlightcolor="black")
        self.contrasenia_entry.configure(insertbackground="black")
        self.contrasenia_entry.configure(selectbackground="#c4c4c4")
        self.contrasenia_entry.configure(selectforeground="black")

        self.frecuencia_entry = Entry(top)
        self.frecuencia_entry.place(relx=0.16, rely=0.26, relheight=0.06
                , relwidth=0.19)
        self.frecuencia_entry.configure(background="white")
        self.frecuencia_entry.configure(disabledforeground="#a3a3a3")
        self.frecuencia_entry.configure(font="TkFixedFont")
        self.frecuencia_entry.configure(foreground="#000000")
        self.frecuencia_entry.configure(highlightbackground="#d9d9d9")
        self.frecuencia_entry.configure(highlightcolor="black")
        self.frecuencia_entry.configure(insertbackground="black")
        self.frecuencia_entry.configure(selectbackground="#c4c4c4")
        self.frecuencia_entry.configure(selectforeground="black")

        self.puerto_entry = Entry(top)
        self.puerto_entry.place(relx=0.53, rely=0.02, relheight=0.06
                , relwidth=0.19)
        self.puerto_entry.configure(background="white")
        self.puerto_entry.configure(disabledforeground="#a3a3a3")
        self.puerto_entry.configure(font="TkFixedFont")
        self.puerto_entry.configure(foreground="#000000")
        self.puerto_entry.configure(highlightbackground="#d9d9d9")
        self.puerto_entry.configure(highlightcolor="black")
        self.puerto_entry.configure(insertbackground="black")
        self.puerto_entry.configure(selectbackground="#c4c4c4")
        self.puerto_entry.configure(selectforeground="black")

        self.ssl_check = Checkbutton(top)
        self.ssl_check.place(relx=0.39, rely=0.12, relheight=0.08, relwidth=0.06)

        self.ssl_check.configure(activebackground="#d9d9d9")
        self.ssl_check.configure(activeforeground="#000000")
        self.ssl_check.configure(background="#f1f1f1")
        self.ssl_check.configure(command=pantalla_support.check_ssl)
        self.ssl_check.configure(disabledforeground="#a3a3a3")
        self.ssl_check.configure(foreground="#000000")
        self.ssl_check.configure(highlightbackground="#d9d9d9")
        self.ssl_check.configure(highlightcolor="black")
        self.ssl_check.configure(justify=LEFT)
        self.ssl_check.configure(text='''SSL''')
        self.ssl_check.configure(variable=pantalla_support.che55)

        self.desconectar_btn = Button(top)
        self.desconectar_btn.place(relx=0.87, rely=0.02, height=70, width=105)
        self.desconectar_btn.configure(activebackground="#d9d9d9")
        self.desconectar_btn.configure(activeforeground="#000000")
        self.desconectar_btn.configure(background="#d9d9d9")
        self.desconectar_btn.configure(command=pantalla_support.desconectar)
        self.desconectar_btn.configure(disabledforeground="#a3a3a3")
        self.desconectar_btn.configure(foreground="#000000")
        self.desconectar_btn.configure(highlightbackground="#d9d9d9")
        self.desconectar_btn.configure(highlightcolor="black")
        self.desconectar_btn.configure(pady="0")
        self.desconectar_btn.configure(text='''Desconectar''')

        self.info_listbox = Listbox(top)
        self.info_listbox.place(relx=0.18, rely=0.45, relheight=0.52
                , relwidth=0.71)
        self.info_listbox.configure(background="white")
        self.info_listbox.configure(disabledforeground="#a3a3a3")
        self.info_listbox.configure(font="TkFixedFont")
        self.info_listbox.configure(foreground="#000000")
        self.info_listbox.configure(highlightbackground="#d9d9d9")
        self.info_listbox.configure(highlightcolor="black")
        self.info_listbox.configure(selectbackground="#c4c4c4")
        self.info_listbox.configure(selectforeground="black")
        self.info_listbox.configure(width=654)

        self.estado_conexion_info = Label(top)
        self.estado_conexion_info.place(relx=0.69, rely=0.22, height=31
                , width=271)
        self.estado_conexion_info.configure(activebackground="#f9f9f9")
        self.estado_conexion_info.configure(activeforeground="black")
        self.estado_conexion_info.configure(anchor=W)
        self.estado_conexion_info.configure(background="#f1f1f1")
        self.estado_conexion_info.configure(disabledforeground="#a3a3a3")
        self.estado_conexion_info.configure(foreground="#8000ff")
        self.estado_conexion_info.configure(highlightbackground="#d9d9d9")
        self.estado_conexion_info.configure(highlightcolor="black")
        self.estado_conexion_info.configure(text='''Desconectado''')

        self.estado_conexion_lb = Label(top)
        self.estado_conexion_lb.place(relx=0.48, rely=0.22, height=31, width=177)

        self.estado_conexion_lb.configure(activebackground="#f9f9f9")
        self.estado_conexion_lb.configure(activeforeground="black")
        self.estado_conexion_lb.configure(anchor=E)
        self.estado_conexion_lb.configure(background="#f1f1f1")
        self.estado_conexion_lb.configure(disabledforeground="#a3a3a3")
        self.estado_conexion_lb.configure(foreground="#000000")
        self.estado_conexion_lb.configure(highlightbackground="#d9d9d9")
        self.estado_conexion_lb.configure(highlightcolor="black")
        self.estado_conexion_lb.configure(text='''Estado conexion:''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.CargarDatosBtn = Button(top)
        self.CargarDatosBtn.place(relx=0.37, rely=0.2, height=42, width=119)
        self.CargarDatosBtn.configure(activebackground="#d9d9d9")
        self.CargarDatosBtn.configure(activeforeground="#000000")
        self.CargarDatosBtn.configure(background="#d9d9d9")
        self.CargarDatosBtn.configure(command=pantalla_support.cargar_datos)
        self.CargarDatosBtn.configure(disabledforeground="#a3a3a3")
        self.CargarDatosBtn.configure(foreground="#000000")
        self.CargarDatosBtn.configure(highlightbackground="#d9d9d9")
        self.CargarDatosBtn.configure(highlightcolor="black")
        self.CargarDatosBtn.configure(pady="0")
        self.CargarDatosBtn.configure(text='''Cargar Datos''')

        self.LimpiarBtn = Button(top)
        self.LimpiarBtn.place(relx=0.37, rely=0.3, height=42, width=118)
        self.LimpiarBtn.configure(activebackground="#d9d9d9")
        self.LimpiarBtn.configure(activeforeground="#000000")
        self.LimpiarBtn.configure(background="#d9d9d9")
        self.LimpiarBtn.configure(command=pantalla_support.limpiar_pantalla)
        self.LimpiarBtn.configure(disabledforeground="#a3a3a3")
        self.LimpiarBtn.configure(foreground="#000000")
        self.LimpiarBtn.configure(highlightbackground="#d9d9d9")
        self.LimpiarBtn.configure(highlightcolor="black")
        self.LimpiarBtn.configure(pady="0")
        self.LimpiarBtn.configure(text='''Limpiar''')
        self.LimpiarBtn.configure(width=118)






if __name__ == '__main__':
    vp_start_gui()



